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

Justin

## Code2AMR

Justin

## AMR Refinement

Justin
