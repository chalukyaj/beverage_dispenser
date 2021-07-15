import os, json
from copy import copy
from beverage_dispenser.services.permutations_generator import PermutationsGenerator
from beverage_dispenser.services.combinations_generator import CombinationsGenerator

os.path.join(os.getcwd(), "beverage_dispenser")


# Class Dispenser
# Holds dispenser configuration and requirements and comes out with possible orders of beverages
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

    # See if the Base Ingredients themselves are sufficient for the beverage
    # If not, it's a drink that can never be prepared no matter the order
    def canBePreparedWithFullQuantity(self, ingredients):
        for ingredient, quantity_required in ingredients.items():
            if ingredient not in self.total_quantity:
                return False, 'not available', ingredient
            elif quantity_required > self.total_quantity[ingredient]:
                return False, 'not sufficient', ingredient
        return True, '', ''

    # Try dispensing the beverages in the order received and check
    # if the base ingredients are insufficient along the way to get beverages
    # which can be prepared
    def try_dispensing_given_order(self, orderOfDrinks):
        quantity = copy(self.total_quantity)

        canDispense = []
        canNotDispense = []
        unavailabilityReason = {}

        ### OUTER LOOP
        for beverage in orderOfDrinks:
            # Make quantity subtraction operations on a temp memory so in case the beverage needs more than
            # available ingredients it can be marked as 'Not Prepared' and the quantity for the other ingredients
            # checked so far is quickly restored to what it was at the end of the previous drink served
            tmpQuantity = copy(quantity)
            # Quantity of corresponding ingredients required by the current beverage
            quantities_required = self.beverages[beverage].items()

            ### INNER LOOP
            for ingredient, quantity_required in quantities_required:
                # Remove the quantity of ingredient needed
                tmpQuantity[ingredient] -= quantity_required

                # Check if the above operation depleted the ingredient
                if tmpQuantity[ingredient] < 0:
                    canNotDispense.append(beverage)
                    unavailabilityReason[beverage] = ingredient
                    # Break out of INNER LOOP if the ingredient was over consumed
                    # This will also prevent from the following `else` block from being executed
                    break
            else:
                # Code reaches here if the preceding loop terminated normally WITHOUT a break
                # Add beverage to the list of beverages that can be dispensed
                canDispense.append(beverage)
                quantity = tmpQuantity
            continue

        # If no drinks can be dispensed than just straight away return
        if not canDispense:
            return

        # Sorting here to make sure the key generated from this is consistent and can identify other orders with same beverages
        # For example Tea, Coffee, Milk == Milk, Coffee, Tea if all three beverages can be prepared
        canDispense.sort()
        canNotDispense.sort()
        # See if there's a set of order where the same beverage set was dispensed
        # In that case, current data is a alternate route to get the same output
        key = json.dumps(canDispense)           # json.dumps([canDispense, canNotDispense])
        self.dispensePossibilities[key] = {
            "can": canDispense,
            "canNot": canNotDispense,
            "unavailabilityReason": unavailabilityReason
        }

    def dispense(self):
        ind = 0
        invalidDrinks = set()
        invalidDrinksMessage = ""
        # Maintain a static message for drinks that cannot be dispensed ever, this will be appended to each OUTPUT
        for beverage, ingredients in self.beverages.items():
            # Check if the beverage can be even prepared will all ingredients at max quantity
            canPrepare, reason, missingIngredient = self.canBePreparedWithFullQuantity(ingredients)
            if not canPrepare:
                invalidDrinks.add(beverage)
                invalidDrinksMessage += f'{self.COLOR_FAIL} ✖ {beverage} cannot be prepared because {missingIngredient} is {reason}\n'
            ind += 1
        # print('Invalid Drinks ', invalidDrinks)

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
        # This is required by the test to check against the expected output
        returnVal = {
            "invalid": invalidDrinks,
            "possibleOrders": []
        }

        # Print all Outputs for possible orders of beverages
        for index in self.dispensePossibilities:
            print(f'{self.COLOR_HEADER}\n\nOutput : {ind}')
            # Drinks which were prepared
            for preparedBeverage in self.dispensePossibilities[index]['can']:
                print(f'{self.COLOR_OK} ✔ {preparedBeverage} is prepared')

            # Drinks which ran out of ingredients
            for unavailableBeverage in self.dispensePossibilities[index]['canNot']:
                print(f'{self.COLOR_FAIL} ✖ {unavailableBeverage} cannot be prepared because {self.dispensePossibilities[index]["unavailabilityReason"][unavailableBeverage]} is not sufficient')

            # Drinks which never could have been prepared
            print(invalidDrinksMessage)

            returnVal['possibleOrders'].append(self.dispensePossibilities)
            ind += 1

        return returnVal


async def configure_dispenser(data: object):
    processor = Dispenser(
        data['outlets']['count_n'],
        data['total_items_quantity'],
        len(data['beverages']),
        data['beverages']
    )

    return processor
