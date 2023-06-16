# SKEMA Architecture Demo

<p><b>FIXME:</b> Include overview text </p>

## Environment
Run this software in a Python virtual environment

<p><b>FIXME:</b>  List the required pip installations </p>

## Before starting

Make sure the bridge network 'asist_net' is running.
```
docker network create asist_net
```

## Start the service containers 

Pull the latest images from docker hub and start them
```
docker-compose pull && docker-compose up -d
```

The following containers should be running
<l>
```
skema-rs
skema-py
img2mml
latex2mml
```
</l>
<p><b>FIXME:</b> Include the mathjax server container</p>

## Testing

Jupyter notebooks are provided for testing. 

<p><b>FIXME:</b> Needs a better description of the testing process</p>
