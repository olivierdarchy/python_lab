# Made to stay sharp in python:
#
# Usage of :
#   - decorators
#   - generators
#   - assert
#   - lambda functions
#
# Exercice : generate a list of bissextiles years between two given limits
#   - input: start, limit
#   - output: array of year
#
# by Olivier Darchy
# created the 23th of September,2017

import time

# lambdas
IS_DIV_BY_4 = lambda num : num % 4 == 0
IS_DIV_BY_100 = lambda num : num % 100 == 0
IS_DIV_BY_400 = lambda num : num % 400 == 0

# slow algorithm
def slow_bissextile_gen(start, limit) :
    """
    generate bissextiles years between start and limit (included).
    /!\ a year is bissextile if it's dividable by 400 or dividable by 4 but not by 100.
    """

    # this function must not works if start is negativ or it start is greater than limit
    assert not (start < 0 or start > limit), "bad usage of slow_bissextile_gen"

    lmt = limit + 1
    for y in range(start, lmt):
        if IS_DIV_BY_400(y) or (IS_DIV_BY_4(y) and not IS_DIV_BY_100(y)) :
            yield y

def slow_get_bissextiles(start=0, limit=100) :
    return [y for y in slow_bissextile_gen(start, limit)]

# fast algorithm
def fast_bissextile_gen(start, limit) :
    """
    generate bissextiles years between start and limit (included).
    /!\ a year is bissextile if it's dividable by 400 or dividable by 4 but not by 100.
    """

    # this function must not works if start is negativ or it start is greater than limit
    assert not (start < 0 or start > limit), "bad usage of fast_bissextile_gen"

    lmt = limit + 1
    strt = start + 4 - start % 4 if start > 0 else 0
    for y in range(strt, lmt, 4):
        if IS_DIV_BY_400(y) or not IS_DIV_BY_100(y) :
            yield y

def fast_get_bissextiles(start=0, limit=100) :
    return [y for y in fast_bissextile_gen(start, limit)]

# -----------------------------------
# tools for tests

class Static_int :
    """
    Represent a static incrementable integer
    """

    def __init__(self, val=0, step=1) :
        self.val = val
        self.step = step

    def inc(self) :
        val = self.val
        self.val += self.step
        return val

test_number = Static_int(1)
MSG = "Dump data {} : {}"

# function decorator
def test_formating(func) :
    def wrapper(*args, **kwargs) :
        assert func(*args, **kwargs), MSG.format(args[0], args[1])
        print("TEST NUMBER {}: OK".format(test_number.inc()))
    return wrapper

@test_formating
def functional_tester(known, actual) :
    return known == actual

@test_formating
def performance_tester(slow, fast) :
    return slow > fast

def timer(func, *args, **kwargs) :
    begin = time.time()
    func(*args, **kwargs)
    end = time.time()
    t = (end - begin) / 1000000000
    print("running {} (about {} loops) take {} ns".format(func.__name__, args[1] - args[0], t))
    return t

# testing
if __name__ == "__main__" :

    print("""\ntesting low algorithm
    \r----------------------------------------
    """)
    functional_tester([0, 4, 8], slow_get_bissextiles(start=0, limit=10))
    functional_tester([], slow_get_bissextiles(start=99, limit=101))
    functional_tester([400, 404], slow_get_bissextiles(start=399, limit=405))

    print("""\ntesting fast algorithm
    \r----------------------------------------
    """)
    functional_tester([0, 4, 8], fast_get_bissextiles(start=0, limit=10))
    functional_tester([], fast_get_bissextiles(start=99, limit=101))
    functional_tester([400, 404], fast_get_bissextiles(start=399, limit=405))

    print("""\ntesting performance
    \r----------------------------------------
    """)
    performance_tester(timer(slow_get_bissextiles, 0, 1000), timer(fast_get_bissextiles, 0, 1000))
    performance_tester(timer(slow_get_bissextiles, 0, 2017), timer(fast_get_bissextiles, 0, 2017))
    performance_tester(timer(slow_get_bissextiles, 0, 10000), timer(fast_get_bissextiles, 0, 10000))

    print("""\nfunctions results
    \r----------------------------------------
    """)
    print("\nslow algorithm starting at 0 until 2017:\n{}".format(slow_get_bissextiles(0, 2017)))
    print("\nfast algorithm starting at 0 until 2017:\n{}".format(fast_get_bissextiles(0, 2017)))
