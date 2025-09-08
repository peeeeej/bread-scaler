import bread
import pytest

from bread import Loaf
from io import StringIO
from unittest.mock import patch

dough_test = Loaf(quantity=3, weight=250, hydration=72, salt=2, starter=12, starter_ratio=1, oil=0)

dough_test_with_starter_ratio = Loaf(
    quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8, oil=0
)
dough_test_with_oil = Loaf(
    quantity=1, weight=250, hydration=72, salt=2, starter=12, starter_ratio=1, oil=3
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


def test_total_oil_returns_correct_amount_of_oil():
    oil_in_recipe = dough_test_with_oil.total_oil
    assert oil_in_recipe == 4.237288135593221


def test_round_to_nearest_half_rounds_to_half_gram():
    rounded_water = bread.Loaf.round_to_nearest_half(244.74)
    assert rounded_water == 244.5


def test_round_to_nearest_half_rounds_to_whole_gram():
    rounded_water = bread.Loaf.round_to_nearest_half(244.75)
    assert rounded_water == 245


def test_total_ingredients_weight_matches_target():
    dough = Loaf(quantity=1, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=1, oil=3)
    total_weight = (
        dough.total_flour_in_recipe
        + dough.total_water_in_recipe
        + dough.total_salt
        + dough.total_starter
        + dough.total_oil
    )
    assert total_weight == 1000


def test_total_ingredients_weight_matches_target_with_ratio():
    dough = Loaf(
        quantity=1, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=0.8, oil=2
    )
    total_weight = (
        dough.total_flour_in_recipe
        + dough.total_water_in_recipe
        + dough.total_salt
        + dough.total_starter
        + dough.total_oil
    )
    assert total_weight == 1000


def test_total_ingredients_weight_matches_target_multiple_loaves():
    dough = Loaf(quantity=20, weight=1000, hydration=80, salt=2, starter=10, starter_ratio=1, oil=1)
    total_weight = (
        dough.total_flour_in_recipe
        + dough.total_water_in_recipe
        + dough.total_salt
        + dough.total_starter
        + dough.total_oil
    )
    expected_weight = dough.weight * dough.quantity
    assert total_weight == pytest.approx(expected_weight, rel=1e-9)


def test_print_recipe_prints_recipe():
    """Test that print_recipe outputs the correct recipe format"""
    dough = Loaf(quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8, oil=0)
    expected_output = (
        "Number of dough balls: 1\n\n"
        "Recipe:\n"
        "Flour: 435.16g\n"
        "Water: 348.13g\n"
        "Salt: 9.89g\n"
        "Starter: 106.81g\n"
    )

    with patch("sys.stdout", new=StringIO()) as fake_output:
        dough.print_recipe(round_to_half=False)
        assert fake_output.getvalue() == expected_output


def test_print_recipe_prints_recipe_with_oil():
    """Test that print_recipe outputs the correct recipe format"""
    dough = Loaf(quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8, oil=1)
    expected_output = (
        "Number of dough balls: 1\n\n"
        "Recipe:\n"
        "Flour: 432.79g\n"
        "Water: 346.23g\n"
        "Salt: 9.84g\n"
        "Starter: 106.23g\n"
        "Oil: 4.92g\n"
    )
    with patch("sys.stdout", new=StringIO()) as fake_output:
        dough.print_recipe(round_to_half=False)
        assert fake_output.getvalue() == expected_output


def test_print_recipe_prints_recipe_rounded():
    """Test that print_recipe outputs the correct recipe format"""
    dough = Loaf(quantity=1, weight=900, hydration=80, salt=2, starter=12, starter_ratio=0.8, oil=0)
    expected_output = (
        "Number of dough balls: 1\n\n"
        "Recipe:\n"
        "Flour: 435.0g\n"
        "Water: 348.0g\n"
        "Salt: 10.0g\n"
        "Starter: 107.0g\n"
    )

    with patch("sys.stdout", new=StringIO()) as fake_output:
        dough.print_recipe(round_to_half=True)
        assert fake_output.getvalue() == expected_output


if __name__ == "__main__":
    pytest.main()
