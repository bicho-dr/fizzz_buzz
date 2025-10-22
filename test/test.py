def test()-> None:
    from src.fizz_buzz import fizz_buzz
    fizz_buzz()

def test_fizzbuzz_returns_number_for_non_multiples():
    result = fizzbuzz(1)
    assert result == "1"