import os
from fastapi import Request
from starlette.responses import JSONResponse
from beverage_dispenser.services.dispenser_service import configure_dispenser

os.path.join(os.getcwd(), "beverage_dispenser")


async def process_dispenser_requirements(request: Request):
    dispenser = await configure_dispenser(request)
    dispenser.dispense()
    return JSONResponse(
        content={"beverage-dispenser": {"status": "up", "requestID": request.state.request_id}},
        status_code=200,
        headers={"content-type": "application/json"},
    )
