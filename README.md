# ASKEM-TA1-DockerVM
Place to create docker recepies that will make our pipelines easy to use

# Usage
The current directory must contain subdirectories `inputs` and `outputs`. Inputs will have plain text files to be processed by TA 1 reading pipelines
Edit `docker-compose.yml` to add your OpenAI API key.

Run `docker compose up` and after both pipelines have finished, the `outputs` directory will contain files with the following prefiexes:
- `extractions_` Arizona output artifacts
- `mit_` MIT output artifacts
- `canonical_` merged outputs using canonical data format

# SKEMA Service Components

## Text Reading

Enrique

## Eqn2AMR

### {Img,LaTeX}2pMML

Liang

### pMML2AMR

There are several endpoints that can be used for this aspect of the workflow. They are demonstrated in the `MORAE_demo.ipynb` notebook in the `morae-demo/` directory. 

1. `put("/mathml/petrinet")` 

	Is a put request takes in a vector of mathml strings and returns an AMR of the PetriNet variety. 
2. `put("/mathml/regnet")`

	Is a put request takes in a vector of mathml strings and returns an AMR of the RegNet variety.
	
3. `put("/mathml/amr")` 

	Is a put request that takes in a JSON like object which includes a vector of mathml strings and a model keyword to indicate the type of AMR wanted out, as below for an example for a regnet:
	`{
    "mathml": [
        "<math><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>alpha</mi><mi>x</mi><mo>-</mo><mi>beta</mi><mi>x</mi><mi>y</mi></mrow></math>",
        "<math><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>delta</mi><mi>x</mi><mi>y</mi><mo>-</mo><mi>gamma</mi><mi>y</mi></mrow></math>"
    ],
    "model": "regnet"
}`


## Code2AMR

### code2FN

Clay/Tito Not sure what endpoints etc.

### FN2AMR

This is demonstrated in the `MORAE_demo.ipynb` notebook in the `morae-demo/` directory.

This part of the workflow currently has two endpoints, one for PertriNets and one for RegNets, however only PetriNet's is supported right now. It is accessed through the following endpoint: 

`put("/models/PN")`

This endpoint takes in a gromet function network JSON (the output of code2FN) and attempts to infer the core dynamics of a PetriNet in it and export them as an AMR. 

In the near future there will be support for RegNets as well via another endpoint.

## AMR Refinement

This is demonstrated in the `MORAE_demo.ipynb` notebook in the `morae-demo/` directory.

Enrique, if you could explain how to run it here. 