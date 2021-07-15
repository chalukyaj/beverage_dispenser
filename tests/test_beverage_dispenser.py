import os, json, pytest
from beverage_dispenser.services.dispenser_service import configure_dispenser

os.path.join(os.getcwd(), "beverage_dispenser")


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


@pytest.mark.asyncio
async def test_input1():
    jsonData = json.load(open('/app/beverage_dispenser/constants/sample_input1.json', 'r'))
    dispenser = await configure_dispenser(jsonData['DATA']['machine'])
    output = dispenser.dispense()

    assert jsonData['OUTPUT'] == json.loads(json.dumps(output, cls=SetEncoder))


@pytest.mark.asyncio
async def test_input2():
    jsonData = json.load(open('/app/beverage_dispenser/constants/sample_input2.json', 'r'))
    dispenser = await configure_dispenser(jsonData['DATA']['machine'])
    output = dispenser.dispense()

    assert jsonData['OUTPUT'] == json.loads(json.dumps(output, cls=SetEncoder))


@pytest.mark.asyncio
async def test_input3():
    jsonData = json.load(open('/app/beverage_dispenser/constants/sample_input3.json', 'r'))
    dispenser = await configure_dispenser(jsonData['DATA']['machine'])
    dispenser.dispense()

    assert jsonData['OUTPUT']
