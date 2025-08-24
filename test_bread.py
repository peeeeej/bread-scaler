import bread
import pytest

from bread import Loaf

dough_test = Loaf(quantity=3, weight=250, hydration=72, salt=2, starter=12, starter_ratio=1)

dough_test_with_starter_ratio = Loaf(
    quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8
)


def test_return_unit_value_returns_correct_unit_value():
    unit_value = dough_test._return_unit_value()
    assert unit_value == 1.4367816091954022


def test_return_starter_multiplier_returns_correct_starter_multiplier():
    starter_multiplier = dough_test._return_starter_multiplier()
    assert starter_multiplier == 0.12


def test_return_amount_of_flour_in_starter_returns_correct_amount():
    amount_in_starter = dough_test._return_amount_of_flour_in_starter()
    assert amount_in_starter == 17.241379310344826


def test_total_flour_in_recipe_returns_correct_amount_of_flour():
    flour_in_recipe = dough_test.total_flour_in_recipe
    assert flour_in_recipe == 379.3103448275862


def test_total_water_in_recipe_returns_correct_amount_of_water():
    water_in_recipe = dough_test.total_water_in_recipe
    assert water_in_recipe == 258.6206896551724


def test_return_water_in_recipe_returns_correct_amount_of_water_with_ratio():
    water_in_recipe = dough_test_with_starter_ratio.total_water_in_recipe
    assert water_in_recipe == 348.13186813186815


def test_total_water_returns_correct_water_in_recipe_with_ratio():
    water_in_starter = dough_test_with_starter_ratio._return_amount_of_water_in_starter(ratio=0.8)
    assert water_in_starter == 47.472527472527474


def test_return_salt_in_recipe_returns_correct_amount_of_salt():
    salt_in_recipe = dough_test.total_salt
    assert salt_in_recipe == 8.620689655172413


def test_return_starter_in_recipe_returns_correct_amount_of_starter():
    starter_in_recipe = dough_test.total_starter
    assert starter_in_recipe == 103.44827586206895


def test_return_starter_in_recipe_returns_correct_amount_of_starter_with_ratio():
    starter_in_recipe = dough_test_with_starter_ratio.total_starter
    assert starter_in_recipe == 106.81318681318682


def test_round_to_nearest_half_rounds_to_half_gram():
    rounded_water = bread.round_to_nearest_half(244.74)
    assert rounded_water == 244.5


def test_round_to_nearest_half_rounds_to_whole_gram():
    rounded_water = bread.round_to_nearest_half(244.75)
    assert rounded_water == 245


def test_total_ingredients_weight_matches_target():
    dough = Loaf(quantity=1, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=1)
    total_weight = round(
        (
            dough.total_flour_in_recipe
            + dough.total_water_in_recipe
            + dough.total_salt
            + dough.total_starter
        ),
        2,
    )
    assert total_weight == 1000


def test_total_ingredients_weight_matches_target_with_ratio():
    dough = Loaf(quantity=1, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=0.8)
    total_weight = round(
        (
            dough.total_flour_in_recipe
            + dough.total_water_in_recipe
            + dough.total_salt
            + dough.total_starter
        ),
        2,
    )
    assert total_weight == 1000


def test_total_ingredients_weight_matches_target_multiple_loaves():
    dough = Loaf(quantity=3, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=1)
    total_weight = round(
        (
            dough.total_flour_in_recipe
            + dough.total_water_in_recipe
            + dough.total_salt
            + dough.total_starter
        ),
        2,
    )
    assert total_weight == 3000


if __name__ == "__main__":
    pytest.main()
