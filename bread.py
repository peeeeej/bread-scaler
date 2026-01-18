"""
Bread Recipe Calculator - Scale recipes using baker's percentages.

This tool converts baker's percentages (ingredient amounts expressed as a percentage
of flour weight) into actual gram measurements for your specific dough weight and
quantity.

Example:
    python bread.py -d 1000 -w 80 -s 2 --starter 10

    Creates a recipe for 1000g of dough with:
    - 80% hydration (water)
    - 2% salt
    - 10% starter (fermented flour)

Usage:
    - Use --starter for sourdough recipes
    - Use --yeast for commercial yeast (pizza, quick breads)
    - Combine with --oil, --sugar for enriched doughs
    - Use --round to round ingredients to nearest 0.5g for practical baking
"""

import argparse


class Loaf:
    def __init__(
        self,
        quantity: int,
        weight: float,
        hydration: float,
        salt: float,
        starter: float = 0,
        starter_ratio: float = 1,
        oil: float = 0,
        sugar: float = 0,
        commercial_yeast: float = 0,
    ) -> None:
        if starter == 0 and commercial_yeast == 0:
            raise ValueError(
                "Recipe must include either starter or commercial yeast. "
                "Provide --starter or --yeast argument."
            )
        self.quantity = quantity
        self.weight = weight
        self.hydration = hydration
        self.salt = salt
        self.starter = starter
        self.starter_ratio = starter_ratio
        self.oil = oil
        self.sugar = sugar
        self.commercial_yeast = commercial_yeast

    def _return_unit_value(self) -> float:
        """
        Needed to determine downstream ingredient amounts based on weight of the loaf,
        hydration and the amount of salt
        """
        return self.weight / (
            100 + (self.hydration + self.salt + self.oil + self.sugar + self.commercial_yeast)
        )

    def _return_starter_multiplier(self) -> float:
        """
        Needed to determine how much of the flour and water in the recipe is coming
        from the starter.
        """
        return self.starter * 0.01

    def _return_amount_of_flour_in_starter(self) -> float:
        """
        Returns the amount of flour in the starter.
        """
        flour_in_starter = (self._return_unit_value() * 100) * self._return_starter_multiplier()
        return flour_in_starter

    def _return_amount_of_water_in_starter(self, ratio: float) -> float:
        """
        Returns the amount of water in the starter. If a starter ratio is not supplied on the
        command line, assume that the amount of water in the starter is equal to the amount of
        flour in the starter.
        """
        water_in_starter = (
            (self._return_unit_value() * 100) * self._return_starter_multiplier()
        ) * ratio
        return water_in_starter

    @property
    def total_flour_in_recipe(self) -> float:
        """
        Returns the amount of flour in the recipe minus the amount of flour in the starter.
        """
        flour_in_recipe = (
            self._return_unit_value() * 100
        ) - self._return_amount_of_flour_in_starter()
        return self.quantity * flour_in_recipe

    @property
    def total_water_in_recipe(self) -> float:
        """
        Returns the amount of water in the recipe minus the amount of water in the starter.
        """
        water_in_recipe = (
            self._return_unit_value() * self.hydration
        ) - self._return_amount_of_water_in_starter(ratio=self.starter_ratio)
        return self.quantity * water_in_recipe

    @property
    def total_salt(self) -> float:
        """
        Returns the amount of salt in the recipe based on the unit value calculation and
        the percent of salt in the loaf.
        """
        return self.quantity * (self._return_unit_value() * self.salt)

    @property
    def total_starter(self) -> float:
        """
        Returns the sum of the amount of flour in starter and the amount of water in starter.
        """
        return self.quantity * (
            self._return_amount_of_flour_in_starter()
            + self._return_amount_of_water_in_starter(ratio=self.starter_ratio)
        )

    @property
    def total_oil(self) -> float:
        """
        Returns the amount of oil in the recipe
        """
        return self.quantity * (self._return_unit_value() * self.oil)

    @property
    def total_sugar(self) -> float:
        """Returns the amount of sugar in the recipe"""
        return self.quantity * (self._return_unit_value() * self.sugar)

    @property
    def total_commercial_yeast(self) -> float:
        """Returns the amount of commercial yeast in the recipe"""
        return self.quantity * (self._return_unit_value() * self.commercial_yeast)

    @staticmethod
    def round_to_nearest_half(number: float) -> float:
        """Takes a number and returns it rounded to the nearest half"""
        return round(number * 2) / 2

    def print_recipe(self, round_to_half: bool = False) -> None:
        """Print the recipe with ingredient weights in grams."""
        ingredients = {
            "flour": self.total_flour_in_recipe,
            "water": self.total_water_in_recipe,
            "salt": self.total_salt,
            "starter": self.total_starter,
            "oil": self.total_oil,
            "sugar": self.total_sugar,
            "commercial_yeast": self.total_commercial_yeast,
        }

        # Round all ingredients
        for key in ingredients:
            ingredients[key] = round(ingredients[key], 2)
            if round_to_half:
                ingredients[key] = self.round_to_nearest_half(ingredients[key])

        # Build recipe output
        recipe = [
            f"Number of dough balls: {self.quantity}\n",
            "Recipe:",
            f"Flour: {ingredients['flour']}g",
            f"Water: {ingredients['water']}g",
            f"Salt: {ingredients['salt']}g",
        ]

        if ingredients["starter"] > 0:
            recipe.append(f"Starter: {ingredients['starter']}g")
        if ingredients["commercial_yeast"] > 0:
            recipe.append(f"Commercial Yeast: {ingredients['commercial_yeast']}g")
        if ingredients["oil"] > 0:
            recipe.append(f"Oil: {ingredients['oil']}g")
        if ingredients["sugar"] > 0:
            recipe.append(f"Sugar: {ingredients['sugar']}g")

        print("\n".join(recipe))


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-q",
    "--quantity",
    type=int,
    dest="quantity",
    default=1,
    required=False,
    help="number of doughballs or loaves",
)
arg_parser.add_argument(
    "-d",
    "--dough-weight",
    type=float,
    dest="weight",
    required=True,
    help="weight per dough ball or loaf in grams",
)
arg_parser.add_argument(
    "-w",
    "--water",
    type=float,
    dest="hydration",
    required=True,
    help="percent hydration",
)
arg_parser.add_argument("-s", "--salt", type=float, dest="salt", required=True, help="percent salt")
arg_parser.add_argument(
    "--starter",
    type=float,
    dest="starter",
    default=0,
    required=False,
    help="percent starter as a portion of fermented flour",
)
arg_parser.add_argument(
    "-o", "--oil", type=float, dest="oil", default=0, required=False, help="percent oil in recipe"
)
arg_parser.add_argument(
    "--sugar", type=float, dest="sugar", default=0, required=False, help="percent sugar in recipe"
)
arg_parser.add_argument(
    "--yeast",
    type=float,
    dest="commercial_yeast",
    default=0,
    required=False,
    help="percent commercial yeast in recipe",
)
arg_parser.add_argument(
    "--round",
    action="store_true",
    dest="round",
    required=False,
    help="round to nearest half gram",
)
arg_parser.add_argument(
    "--ratio",
    type=float,
    dest="ratio",
    default=1,
    help="use if your starter does not contain equal parts flour and water. this should "
    "be the amount of water compared to flour, e.g. `.8` for 4 parts water to 5 parts "
    "flour.",
)


def main():
    parsed_args = arg_parser.parse_args()

    dough = Loaf(
        quantity=parsed_args.quantity,
        weight=parsed_args.weight,
        hydration=parsed_args.hydration,
        salt=parsed_args.salt,
        starter=parsed_args.starter,
        starter_ratio=parsed_args.ratio,
        oil=parsed_args.oil,
        sugar=parsed_args.sugar,
        commercial_yeast=parsed_args.commercial_yeast,
    )

    dough.print_recipe(round_to_half=parsed_args.round)


if __name__ == "__main__":
    main()
