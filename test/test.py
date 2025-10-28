from src.fizz_buzz import fizz_buzz



def test_number_3_returns_fizz():

    assert fizz_buzz(3) == "fizz"
def test_number_5_returns_fizz():

    assert fizz_buzz(5) == "buzz"

def test_number_15_return_fizzbuzz():
    assert fizz_buzz(15) == "fizzbuzz"


