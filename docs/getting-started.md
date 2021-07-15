## Get started

Env variables come from .env file. No .env.sample as this is for an assigment and the app is supposed to run as is.

For rebuilding, use `docker-compose up --build`. Pass `-d` if you want to run this in the background

SSH into the container by running `docker exec -it beverage_dispenser_dispenser_api_1 /bin/bash`

RUN Tests and return captured output `docker exec beverage_dispenser_dispenser_api_1 /app/run-tests.sh`

NOTE: The container name `beverage_dispenser_dispenser_api_1` can change on your machine, please use `docker ps` to get the list of running containers and get the name of this container from there.

### Run the application

The server which hosts the api to take in inputs and print output on stdout is already running at the time of docker startup.
If you need you can hit the api hosted at localhost:5000 with the sample input jsons, please note to only use the DATA key's value in the json and the not the entirety of it.
