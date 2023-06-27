# -*- coding: utf-8 -*-
"""
Convert the LaTeX equation to the corresponding presentation MathML using the MathJAX service.
Please run the following command to initialize the MathJAX service:
node data_generation/mathjax_server.js
"""

from typing import Text, Union
from typing_extensions import Annotated
from fastapi import FastAPI, Body, File, Response, Request, Query
from skema.img2mml.api import (get_mathml_from_bytes, get_mathml_from_latex)
from skema.data.eq2mml import img_b64_bayes_white_bg
from pydantic import BaseModel, Field
import base64

EquationQueryParameter = Annotated[
  Text,
  Query(
      examples={
          "simple": {
              "summary": "A familiar equation",
              "description": "A simple equation (mass-energy equivalence)",
              "value": "E = mc^{2}",
          },
          "complex": {
              "summary": "A more feature-rich equation (Bayes' rule)",
              "description": "A equation drawing on latex features",
              "value": "\\frac{P(\\textrm{a } | \\textrm{ b}) \\times P(\\textrm{b})}{P(\\textrm{a})}",
          }
      },
  ),
]

ImageBytes = Annotated[
  bytes,
  File(
      description="bytes of a PNG of an equation",
      # examples={
      #     "bayes-rule": {
      #         "summary": "PNG of Bayes' rule",
      #         "description": "PNG of Bayes' rule",
      #         "value": str(img_path_bayes_rule_eqn),
      #     }
      # },
  ),
]

class LatexEquation(BaseModel):
    tex_src: Text = Field(title="LaTeX equation", description="The LaTeX equation to process")
    class Config:
        schema_extra = {
            "example": {
                "tex_src": "E = mc^{c}",
            }
        }


app = FastAPI()

def process_latex_equation(eqn: Text) -> Response:
    """Helper function used by both GET and POST LaTeX equation processing endpoints"""
    res = get_mathml_from_latex(eqn)
    return Response(content=res, media_type="application/xml")

# FIXME: have this test the mathjax endpoint (and perhaps check the pt model loaded)
@app.get("/healthcheck", summary="Ping endpoint to test health of service", response_model=Text, status_code=200)
def healthcheck():
    return "The eq2mml service is running."

@app.post("/image/mml", summary="Get MathML representation of an equation image")
async def post_image_to_mathml(data: ImageBytes) -> Response:
    """
    Endpoint for generating MathML from an input image.

    ### Python example
    ```
    import requests

    files = {
      "data": open("bayes-rule-white-bg.png", "rb"),
    }
    r = requests.post("http://0.0.0.0:8000/image/mml", files=files)
    print(r.text)
    """
    # convert bytes of png image to tensor
    res =  get_mathml_from_bytes(data)
    print(res)
    print(type(res))
    return Response(content=res, media_type="application/xml")

@app.post("/image/base64/mml", summary="Get MathML representation of an equation image")
async def post_b64image_to_mathml(request: Request) -> Response:
    """
    Endpoint for generating MathML from an input image.

    ### Python example
    ```
    from pathlib import Path
    import base64
    import requests

    url = "http://0.0.0.0:8000/image/base64/mml"
    with Path("bayes-rule-white-bg.png").open("rb") as infile:
      img_bytes = infile.read()
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    r = requests.post(url, data=img_b64)
    print(r.text)
    """
    img_b64 = await request.body()
    img_bytes = base64.b64decode(img_b64)
    # convert bytes of png image to tensor
    res =  get_mathml_from_bytes(img_bytes)
    return Response(content=res, media_type="application/xml")

@app.get("/latex/mml", summary="Get MathML representation of a LaTeX equation")
async def get_tex_to_mathml(tex_src: EquationQueryParameter) -> Response:
    """
    GET endpoint for generating MathML from an input LaTeX equation.

    ### Python example
    ```
    import requests

    r = requests.get("http://0.0.0.0:8000/latex/mml", params={"tex_src":"E = mc^{c}"})
    print(r.text)
    """
    return process_latex_equation(tex_src)

@app.post("/latex/mml", summary="Get MathML representation of a LaTeX equation")
async def post_tex_to_mathml(eqn: LatexEquation) -> Response:
    """
    Endpoint for generating MathML from an input LaTeX equation.

    ### Python example
    ```
    import requests

    r = requests.post("http://0.0.0.0:8000/latex/mml", json={"tex_src":"E = mc^{c}"})
    print(r.text)
    """
    # convert latex string to presentation mathml
    return process_latex_equation(eqn.tex_src)
