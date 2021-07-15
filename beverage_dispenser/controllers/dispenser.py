import os
from fastapi import Request
from starlette.responses import JSONResponse
from beverage_dispenser.services.dispenser_service import configure_dispenser

os.path.join(os.getcwd(), "beverage_dispenser")


async def process_dispenser_requirements(request: Request):
    ## Get Dispenser Service Object
    dispenser = await configure_dispenser((await request.json())['machine'])

    # Print all possible dispensing orders on the STDOUT
    dispenser.dispense()

    # Dummy status Ok response
    return JSONResponse(
        content={"beverage-dispenser": {"status": "up", "requestID": request.state.request_id}},
        status_code=200,
        headers={"content-type": "application/json"},
    )
