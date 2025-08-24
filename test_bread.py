import bread
import pytest

from bread import Loaf

dough_test = Loaf(quantity=3, weight=250, hydration=72, salt=2, starter=12)

dough_test_with_starter_ratio = Loaf(
    quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8
)


def test_return_unit_value_returns_correct_unit_value():
    unit_value = dough_test.return_unit_value()
    assert unit_value == 1.44


def test_return_starter_multiplier_returns_correct_starter_multiplier():
    starter_multiplier = dough_test.return_starter_multiplier()
    assert starter_multiplier == 0.12


def test_return_amount_of_flour_in_starter_returns_correct_amount():
    amount_in_starter = dough_test.return_amount_of_flour_in_starter()
    assert amount_in_starter == 17.28


def test_return_flour_in_recipe_returns_correct_amount_of_flour():
    flour_in_recipe = dough_test.return_flour_in_recipe()
    assert flour_in_recipe == 380.16


def test_return_water_in_recipe_returns_correct_amount_of_water():
    water_in_recipe = dough_test.return_water_in_recipe()
    assert water_in_recipe == 259.2


def test_return_water_in_recipe_returns_correct_amount_of_water_with_ratio():
    water_in_recipe = dough_test_with_starter_ratio.return_water_in_recipe()
    assert water_in_recipe == 348.48


def test_return_salt_in_recipe_returns_correct_amount_of_salt():
    salt_in_recipe = dough_test.return_salt_in_recipe()
    assert salt_in_recipe == 8.64


def test_return_starter_in_recipe_Returns_correct_amount_of_starter():
    starter_in_recipe = dough_test.return_starter_in_recipe()
    assert starter_in_recipe == 103.68


def test_round_to_nearest_half_rounds_to_half_gram():
    rounded_water = bread.round_to_nearest_half(244.74)
    assert rounded_water == 244.5


def test_round_to_nearest_half_rounds_to_whole_gram():
    rounded_water = bread.round_to_nearest_half(244.75)
    assert rounded_water == 245


if __name__ == "__main__":
    pytest.main()
