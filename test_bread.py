import pytest

from bread import Loaf

bread = Loaf(quantity=3, weight=250, hydration=72, salt=2, starter=12)

def test_return_unit_value_returns_correct_unit_value():
    unit_value = bread.return_unit_value()
    assert unit_value == 1.44

def test_return_starter_multiplier_returns_correct_starter_multiplier():
    starter_multiplier = bread.return_starter_multiplier()
    assert starter_multiplier == .12

def test_return_amount_of_water_and_flour_in_starter_returns_correct_amount():
    amount_in_starter = bread.return_amount_of_water_and_flour_in_starter()
    assert amount_in_starter == 17.28

def test_return_flour_in_recipe_returns_correct_amount_of_flour():
    flour_in_recipe = bread.return_flour_in_recipe()
    assert flour_in_recipe == 380.16

def test_return_water_in_recipe_returns_correct_amount_of_water():
    water_in_recipe = bread.return_water_in_recipe()
    assert water_in_recipe == 259.2

def test_return_salt_in_recipe_returns_correct_amount_of_salt():
    salt_in_recipe = bread.return_salt_in_recipe()
    assert salt_in_recipe == 8.64

def test_return_starter_in_recipe_Returns_correct_amount_of_starter():
    starter_in_recipe = bread.return_starter_in_recipe()
    assert starter_in_recipe == 103.68

if __name__ == "__main__":
    pytest.main()