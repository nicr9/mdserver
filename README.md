# Markdown Note Server

## Prerequisites

* Docker
* A folder with some markdown notes (e.g. `~/notes/*.md`)

## Build your own

First, build a fresh copy of the image:

```bash
docker build -t mdserver .
```

Here's the docker command to run the server:

```bash
docker run -dp 4000:4000 -v /home/$USER/notes:/opt/notes mdserver
```
