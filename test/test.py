from src.fizz_buzz import fizz_buzz

def test()-> None:
    fizz_buzz()

def test_number_3_returns_fizz():

    assert fizz_buzz(3) == "fizz"

