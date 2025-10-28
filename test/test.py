from src.fizz_buzz import fizz_buzz
import pytest



@pytest.mark.parametrize(
    "n, expected_result",
    [
        (3, "fizz"),

        (5, "buzz"),

        (15, "fizzbuzz"),


    ]
)
def test_FizzBuzz_n_return_expect_result(n: int, expected_result: str):
    assert fizz_buzz(n) == expected_result

