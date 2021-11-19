# unit tests for Fraction class with operator overloading
# this is a start, students will be expected to add the unit tests needed to finish testing their Fraction Class operators: -, *, /, =, ==, <, >, +=, negate operator, ~ (inversion)


from fractions import Fraction

def test_create2int():
    f = Fraction(1, 4)
    assert str(f) == "1/4"

def test_create2int_negative_num():
    f = Fraction(-1,4)
    assert str(f) == "-1/4"

def test_create2int_negative_den():
    f = Fraction(1,-4)
    assert str(f) == "-1/4"

def test_create2int_negative_negative():
    f = Fraction(-1,-4)
    assert str(f) == "1/4"

def test_create2int_reduced():
    f = Fraction(50, 75)
    assert str(f) == "2/3"

def test_create1int():
    f = Fraction(55)
    assert str(f) == "55"

def test_create1int_negative():
    f = Fraction(-65)
    assert str(f) == "-65"

def test_create_float():
    f = Fraction(0.85)
    assert str(f) == "17/20"

def test_create_float_negative():
    f = Fraction(-0.85)
    assert str(f) == "-17/20"

def test_add():
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    f3 = f1 + f2
    assert str(f3) == "5/4"

# place remaining well-named unit tests here
