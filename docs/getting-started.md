## Get started

Env variables come from .env file. No .env.sample as this is for an assigment and the app is supposed to run as is.

For rebuilding, use `docker-compose up --build`.

SSH into the container by running `docker-compose exec serverless /bin/ash`

### Run the application

You can run `moody run` command to start the application server which is available at port `3000`. 

If you want to simulate the actual Lambda environment, for example, to see authorizer in action before actual APIs are hit, you may use `sls offline` to start the Serverless based application server. 

> Note: Only run one server at a time to avoid performance issues.
