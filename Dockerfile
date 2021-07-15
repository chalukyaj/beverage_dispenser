FROM python:3.8-slim

RUN apt-get update
# Install base python dependencies
RUN apt-get install build-essential libssl-dev libffi-dev -y
RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app
COPY . .
RUN poetry install
#ENTRYPOINT [ "/app/server.sh" ]
ENTRYPOINT [ "tail", "-f", "/dev/null" ]
EXPOSE 5000
