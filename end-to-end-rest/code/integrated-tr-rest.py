# Client code for SKEMA TR
from pydantic import BaseModel
import requests, os
import json
import itertools as it
import tempfile
from typing import Any, Dict, List, Union
from pathlib import Path
from typing import Optional, Dict, Any
from askem_extractions.importers import import_arizona, import_mit
from askem_extractions.importers.mit import merge_collections
from askem_extractions.data_model import AttributeCollection

from fastapi import FastAPI, Query

app = FastAPI()


def annotate_text_with_skema(text:Union[str, List[str]]) -> List[Dict[str, Any]]:
	endpoint = f"{os.environ['SKEMA_HOST']}/textFileToMentions"
	if isinstance(text, str):
		payload = [text] # If the text to annotate is a single string representing the contents of a document, make it a list with a single element
	else:
		payload = text # if the text to annotate is already a list of documents to annotate, it is the payload itself
	response = requests.post(endpoint, json=payload, timeout=600)
	if response.status_code == 200:
		return response.json()
	else:
		raise RuntimeError(f"Calling {endpoint} failed with HTTP code {response.status_code}")
	

# Client code for MIT TR

def annotate_text_with_mit(texts:Union[str, List[str]]) -> List[Dict[str, Any]]:
	endpoint = f"{os.environ['MIT_HOST']}/annotation/find_text_vars/"
	if isinstance(texts, str):
		texts = [texts] # If the text to annotate is a single string representing the contents of a document, make it a list with a single element
	
	# TODO paralelize this
	return_values = list()
	for ix, text in enumerate(texts):
		params = {
			"gpt_key": os.environ['OPENAI_KEY'],
			"text": text
		}
		response = requests.post(endpoint, params=params)
		if response.status_code == 200:
			return_values.append(response.json())
		else:
			raise RuntimeError(f"Calling {endpoint} on the {ix}th input failed with HTTP code {response.status_code}")
	return return_values


def normalize_extractions(
        arizona_extractions:Optional[Dict[str, Any]],
        mit_extractions:Optional[Dict]
    ) -> AttributeCollection:
    collections = list()
    with tempfile.TemporaryDirectory() as tmpdirname:
        
        skema_path = os.path.join(tmpdirname, "skema.json")
        mit_path = os.path.join(tmpdirname, "mit.json")

        if arizona_extractions:
            try:
                with open(skema_path, "w") as f:
                    json.dump(arizona_extractions, f)
                canonical_arizona = import_arizona(Path(skema_path))
                collections.append(canonical_arizona)
            except Exception as ex:
                print(ex)
        if mit_extractions:
            try:
                with open(mit_path, "w") as f:
                    json.dump(mit_extractions, f)
                canonical_mit = import_mit(Path(mit_path))
                collections.append(canonical_mit)
            except Exception as ex:
                print(ex)

        if arizona_extractions and mit_extractions:
            # Merge both with some de de-duplications
            params = {
                "gpt_key": os.environ['OPENAI_KEY']
            }

            data = {
                "mit_file": open(mit_path).read(),
                "arizona_file": open(skema_path).read()
            }
            response = requests.post(f"{os.environ['MIT_HOST']}/integration/get_mapping", params=params, data=data)

            if response.status_code == 200:
                map_data = response.text()
                map_path = os.path.join(tmpdirname, "mapping.txt")
                with open(map_path, 'w')as f:
                    f.write(map_data)
                merged_collection = \
                    merge_collections(
                        a_collection=collections[0],
                        m_collection=collections[1],
                        map_path=Path(map_path)
                    )
                
                # Return the merged collection here
                return merged_collection
            

    # Merge the colletions into a attribute collection
    attributes = list(it.chain.from_iterable(c.attributes for c in collections))

    return AttributeCollection(attributes=attributes)

class Documents(BaseModel):
    texts: List[str]
    
@app.post("/integrated_text_extractions/")
async def integrated_text_extractions(
    	texts:Documents,
        annotate_skema:bool = True,
        annotate_mit:bool = True
    ) -> List[AttributeCollection]:
    
    texts = texts.texts
    skema_extractions = [[] for t in texts]

    try:
        skema_extractions = annotate_text_with_skema(texts)
    except Exception as ex:
        print(f"Problem annotating with Skema: {ex}")
        

    mit_extractions = [[] for t in texts]

    try:
        mit_extractions = annotate_text_with_mit(texts)
    except Exception as ex:
        print(f"Problem annotating with MIT: {ex}")
        

    results = list()
    for skema, mit in zip(skema_extractions, mit_extractions):
        normalized = normalize_extractions(arizona_extractions=skema, mit_extractions=mit)
        results.append(normalized)
    return results