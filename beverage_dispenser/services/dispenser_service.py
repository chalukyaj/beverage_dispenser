import os, json
from copy import copy
from fastapi import Request
from beverage_dispenser.providers.mongo import MongoDB
from beverage_dispenser.services.permutations_generator import PermutationsGenerator
from beverage_dispenser.services.combinations_generator import CombinationsGenerator

os.path.join(os.getcwd(), "beverage_dispenser")


class Dispenser:
    COLOR_OK = '\033[92m'
    COLOR_FAIL = '\033[91m'
    COLOR_HEADER = '\033[93m'

    def __init__(
                self,
                nozzles: int,
                total_quantity: object,
                total_beverages: int,
                beverages: object
            ):
        self.nozzles = nozzles
        self.total_quantity = total_quantity
        self.total_beverages = total_beverages
        self.beverages = beverages
        self.dispensePossibilities = {}

    def canBePreparedWithFullQuantity(self, ingredients):
        for ingredient, quantity_required in ingredients.items():
            if ingredient not in self.total_quantity:
                return False, 'not available', ingredient
            elif quantity_required > self.total_quantity[ingredient]:
                return False, 'not sufficient', ingredient
        return True, '', ''

    def try_dispensing_given_order(self, orderOfDrinks):
        quantity = copy(self.total_quantity)

        canDispense = []
        canNotDispense = []
        unavailabilityReason = {}
        for beverage in orderOfDrinks:
            tmpQuantity = copy(quantity)
            quantities_required = self.beverages[beverage].items()
            for ingredient, quantity_required in quantities_required:
                tmpQuantity[ingredient] -= quantity_required
                if tmpQuantity[ingredient] < 0:
                    canNotDispense.append(beverage)
                    unavailabilityReason[beverage] = ingredient
                    break
            else:
                # Check for last quantity
                if tmpQuantity[ingredient] < 0:
                    canNotDispense.append(beverage)
                    unavailabilityReason[beverage] = ingredient
                    continue
                canDispense.append(beverage)
                quantity = tmpQuantity
            continue
        if not canDispense:
            return

        canDispense.sort()
        canNotDispense.sort()
        key = json.dumps([canDispense, canNotDispense])
        self.dispensePossibilities[key] = {
            "can": canDispense,
            "canNot": canNotDispense,
            "unavailabilityReason": unavailabilityReason
        }

    def dispense(self):
        ind = 0
        invalidDrinks = set()
        invalidDrinksMessage = ""

        for beverage, ingredients in self.beverages.items():
            canPrepare, reason, missingIngredient = self.canBePreparedWithFullQuantity(ingredients)
            if not canPrepare:
                invalidDrinks.add(beverage)
                invalidDrinksMessage += f'{self.COLOR_FAIL} ✖ {beverage} cannot be prepared because {missingIngredient} is {reason}\n'
            ind += 1
        print('Invalid Drinks ', invalidDrinks)

        combinationsFor = set(self.beverages.keys())
        combinationsFor -= invalidDrinks
        combinations = CombinationsGenerator(combinationsFor)
        combinations.generate()
        combos = combinations.getCombinations(self.nozzles)

        for combo in combos:
            permutationsGenerator = PermutationsGenerator(combo)
            permutations = permutationsGenerator.generate()
            for permutation in permutations:
                self.try_dispensing_given_order(permutation)

        ind = 1
        for index in self.dispensePossibilities:
            print(f'{self.COLOR_HEADER}\n\nOutput : {ind}')
            for preparedBeverage in self.dispensePossibilities[index]['can']:
                print(f'{self.COLOR_OK} ✔ {preparedBeverage} is prepared')
            for unavailableBeverage in self.dispensePossibilities[index]['canNot']:
                print(f'{self.COLOR_FAIL} ✖ {unavailableBeverage} cannot be prepared because {self.dispensePossibilities[index]["unavailabilityReason"][unavailableBeverage]} is not sufficient')
            print(invalidDrinksMessage)
            ind += 1


async def configure_dispenser(request: Request):
    data = (await request.json())['machine']

    processor = Dispenser(
        data['outlets']['count_n'],
        data['total_items_quantity'],
        len(data['beverages']),
        data['beverages']
    )

    return processor
