# SKEMA end-to-end

This example demonstrates end-to-end ASKEM workflows centered around SKEMA system components.

[See these slides for an overview of the system architecture](https://docs.google.com/presentation/d/115TErFsAiVWf34D3cUYmdoy4SFahrUTzVSvPZlGFTbI)

## Requirements

- Docker
- `docker-compose`
- 26G+ of RAM 
  - NOTE: 20G out of 26G is devoted to the text-reading (`skema-tr`) service

## Start the service containers 

Pull the latest images from docker hub and start the services:

```bash
docker-compose pull && docker-compose up
```

The following containers should be running:

`skema-rs`
`skema-py`
`mathjax`

Open your browser to [http://127.0.0.1:7777](http://127.0.0.1:7777) to view the example notebooks.