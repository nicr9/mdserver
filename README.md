# Markdown Note Server

## Prerequisites

* Docker
* A folder with some markdown notes (e.g. `~/notes/*.md`)

## Pulling from Docker Hub

If you don't wanna waste time building your own, you can get started with this:

```bash
docker pull nicr9/mdserver
docker run -dp 4000:4000 -v /home/$USER/notes:/opt/notes nicr9/mdserver
```

## Build your own

First, build a fresh copy of the image:

```bash
docker build -t mdserver .
```

Here's the docker command to run the server:

```bash
docker run -dp 4000:4000 -v /home/$USER/notes:/opt/notes mdserver
```
