import os

from fastapi import APIRouter, Request
from beverage_dispenser.controllers.dispenser import process_dispenser_requirements


os.path.join(os.getcwd(), "beverage_dispenser")

router = APIRouter()


#######################################
#       Beverage Dispenser APIS       #
#######################################


@router.post("/dispense")
async def getActions(request: Request):
    return await process_dispenser_requirements(request)
