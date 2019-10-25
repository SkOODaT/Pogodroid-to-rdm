# PogoDroid to RDM

<strong>The contents of this repo is a proof of concept and is for educational use only!</strong>

## PogoDroid config

- Enable send raw data
- Add endpoint to pogodroid-to-rdm: http://youserver:5000/raw

## Install

- Check docker-compose and edit RDM_URL: http://yourserver:9001/raw 

## Add to RDM docker-compose

- Add the following code to RDM's docker-compose:

```
services:
...
  pogodroid_to_rdm:
    build: pogodroid-to-rdm/
    tty: true
    restart: unless-stopped
    ports:
      - 5000:5000
    container_name: pogodroid-to-rdm
    environment:
      - RDM_URL=http://realdevicemap:9001/raw
    command: ["app.py"]
```
