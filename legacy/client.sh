#!/bin/bash

while read FILE
do
	NAME=$(basename $FILE)
	OUTPUT="./outputs/mit_$NAME"
	curl -X 'POST' \
		"http://localhost:8000/annotation/upload_file_extract/?gpt_key=$OPENAI_KEY" \
		-H 'accept: application/json' \
		-H 'Content-Type: multipart/form-data' \
		-F "file=@$FILE;type=text/plain" > "$OUTPUT"
done < <(find ./inputs -type f)
