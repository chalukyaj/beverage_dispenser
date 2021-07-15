#!/bin/bash
poetry run uvicorn beverage_dispenser:app --host 0.0.0.0 --port 5000 --reload --log-level info #> server_uvicorn.log
