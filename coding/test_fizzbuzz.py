from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(3*5) == "fizzbuzz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(2) == 2
