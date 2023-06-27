# SKEMA end-to-end

This example demonstrates end-to-end ASKEM workflows centered around SKEMA system components.

**TODO: add link to architecture diagram**

## Requirements

- Docker
- `docker-compose`
- 12G+ of RAM

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