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

Make sure you are in the docker_integration git branch
```
git checkout docker_integration
```

## Start the services 

The following command will pull the latest images from docker hub and start them
```
docker-compose pull && docker-compose up -d
```

## Testing

Jupyter notebooks are provided for testing.  Currently these are in ~/ASKEM-TA1-DockerVM/skema/notebooks

