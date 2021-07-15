## Testing

Pytest based tests for both unit and feature testing.

You may run `docker exec beverage_dispenser_dispenser_api_1 /app/run-tests.sh` to run the full suite of tests

All the tests are stored in `tests` directory

Sample output:

```bash

----------------------------- Captured stdout call -----------------------------


Output : 1
 ✔ hot_coffee is prepared
 ✔ hot_tea is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ green_tea cannot be prepared because green_mixture is not available



Output : 2
 ✔ black_tea is prepared
 ✔ hot_coffee is prepared
 ✖ hot_tea cannot be prepared because hot_water is not sufficient
 ✖ green_tea cannot be prepared because green_mixture is not available



Output : 3
 ✔ black_tea is prepared
 ✔ hot_tea is prepared
 ✖ hot_coffee cannot be prepared because hot_water is not sufficient
 ✖ green_tea cannot be prepared because green_mixture is not available

_________________________________ test_input2 __________________________________
----------------------------- Captured stdout call -----------------------------


Output : 1
 ✔ green_tea is prepared
 ✔ hot_tea is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient



Output : 2
 ✔ green_tea is prepared
 ✔ hot_water is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient



Output : 3
 ✔ black_tea is prepared
 ✔ green_tea is prepared
 ✖ hot_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient



Output : 4
 ✔ hot_tea is prepared
 ✔ hot_water is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ green_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient



Output : 5
 ✔ black_tea is prepared
 ✔ hot_tea is prepared
 ✖ green_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient

_________________________________ test_input3 __________________________________
----------------------------- Captured stdout call -----------------------------


Output : 1
 ✔ black_coffee is prepared
 ✔ hot_coffee is prepared
 ✖ black_tea cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_tea cannot be prepared because hot_milk is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 2
 ✔ black_coffee is prepared
 ✔ green_tea is prepared
 ✔ hot_tea is prepared
 ✖ black_tea cannot be prepared because sugar_syrup is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 3
 ✔ hot_water is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ green_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_water is not sufficient
 ✖ hot_tea cannot be prepared because hot_water is not sufficient



Output : 4
 ✔ black_coffee is prepared
 ✔ black_tea is prepared
 ✔ green_tea is prepared
 ✖ hot_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 5
 ✔ black_tea is prepared
 ✔ hot_tea is prepared
 ✖ green_tea cannot be prepared because sugar_syrup is not sufficient
 ✖ hot_coffee cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 6
 ✔ black_coffee is prepared
 ✔ hot_tea is prepared
 ✖ black_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_coffee cannot be prepared because hot_milk is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 7
 ✔ black_coffee is prepared
 ✔ black_tea is prepared
 ✖ hot_coffee cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_tea cannot be prepared because hot_water is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 8
 ✔ hot_coffee is prepared
 ✖ black_tea cannot be prepared because ginger_syrup is not sufficient
 ✖ green_tea cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_tea cannot be prepared because hot_milk is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 9
 ✔ green_tea is prepared
 ✔ hot_tea is prepared
 ✖ black_tea cannot be prepared because sugar_syrup is not sufficient
 ✖ hot_coffee cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient



Output : 10
 ✔ black_tea is prepared
 ✔ green_tea is prepared
 ✖ hot_coffee cannot be prepared because ginger_syrup is not sufficient
 ✖ hot_tea cannot be prepared because sugar_syrup is not sufficient
 ✖ hot_water cannot be prepared because hot_water is not sufficient

============================== 3 passed in 0.16s ===============================

```
