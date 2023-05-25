FROM python:3.9-bullseye
# Set up the workdir and copy the environment
WORKDIR /app
COPY client.sh /app
CMD ["/bin/bash", "./client.sh"]