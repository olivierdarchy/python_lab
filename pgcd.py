# Made to stay sharp in python:
#
# Exercice : design an algorithm to evaluate the pgcd of two natural integers
#   - input: a, b for a, b € N*
#   - output: pgcd
#
# by Olivier Darchy
# created the 23th of September,2017

def eval_pgcd(a, b) :
    """
    Evaluate and return the greatest comon divisor of two number.
    Use Euclide algorithm to do so
    """

    # verify if a and/or b are not equal to zero (bit shift trick)
    if a << b == a :
        raise ValueError("given number must be defined on N*")

    divisor, divided = (a, b) if a <= b else (b, a)
    carry = -1
    pgcd = 0

    while carry != 0 :
        pgcd = divisor
        carry = divided % divisor
        divided = divisor
        divisor = carry

    return pgcd

# testing
# TODO: encapsulation of testing tools

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
def equal_relation_test(known, actual) :
    return known == actual

if __name__ == "__main__" :
    equal_relation_test(7, eval_pgcd(14, 21))
    equal_relation_test(7, eval_pgcd(21, 14))
    equal_relation_test(21, eval_pgcd(1071, 1029))

    print("PGCD({}, {}) = {}".format(21, 21, eval_pgcd(21, 21)))
    print("PGCD({}, {}) = {}".format(4620, 6625, eval_pgcd(4620, 6625)))
    print("PGCD({}, {}) = {}".format(10884, 8058, eval_pgcd(10884, 8058)))

    try :
        eval_pgcd(5, 0)
    except ValueError as e:
        print(e)
