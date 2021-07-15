## Testing

Pytest based tests for both unit and feature testing.

You may run `moody test` to run the full suite of tests or pass a flag as an option to run either `unit` or `feature` tests.

All the tests are stored in `tests` directory under either `unit` or `feature` depending upon the type of functionality being tested.

Sample output:

```bash

======================================== test session starts ========================================
platform linux -- Python 3.8.2, pytest-5.2.2, py-1.8.0, pluggy-0.13.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
plugins: cov-2.8.1
collected 4 items

tests/test_sample.py::test_answer PASSED                                                      [ 25%]
tests/feature/test_feature.py::test_hello PASSED                                              [ 50%]
tests/unit/test_users.py::test_sum PASSED                                                     [ 75%]
tests/unit/test_users.py::test_sum_zero PASSED                                                [100%]

========================================= 4 passed in 0.09s =========================================

```
