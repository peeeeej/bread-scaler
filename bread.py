import argparse


class Loaf:
    def __init__(
        self,
        quantity: int,
        weight: float,
        hydration: float,
        salt: float,
        starter: float,
        starter_ratio: float,
    ) -> None:
        self.quantity = quantity
        self.weight = weight
        self.hydration = hydration
        self.salt = salt
        self.starter = starter
        self.starter_ratio = starter_ratio

    def _return_unit_value(self) -> float:
        """
        Needed to determine downstream ingredient amounts based on weight of the loaf,
        hydration and the amount of salt
        """
        unit_value = self.weight / (100 + (self.hydration + self.salt))
        return unit_value

    def _return_starter_multiplier(self) -> float:
        """
        Needed to determine how much of the flour and water in the recipe is coming
        from the starter.
        """
        starter_multipler = self.starter * 0.01
        return starter_multipler

    def _return_amount_of_flour_in_starter(self) -> float:
        """
        Returns the amount of flour in the starter.
        """
        unit_value = self._return_unit_value()
        starter_multiplier = self._return_starter_multiplier()
        flour_in_starter = (unit_value * 100) * starter_multiplier
        return flour_in_starter

    def _return_amount_of_water_in_starter(self, ratio) -> float:
        """
        Returns the amount of water in the starter. If a starter ratio is not supplied on the
        command line, assume that the amount of water in the starter is equal to the amount of
        flour in the starter.
        """
        unit_value = self._return_unit_value()
        starter_multiplier = self._return_starter_multiplier()
        water_in_starter = ((unit_value * 100) * starter_multiplier) * ratio
        return water_in_starter

    @property
    def total_flour_in_recipe(self) -> float:
        """
        Returns the amount of flour in the recipe minus the amount of flour in the starter.
        """
        flour_in_starter = self._return_amount_of_flour_in_starter()
        unit_value = self._return_unit_value()
        flour_in_recipe = (unit_value * 100) - flour_in_starter
        return self.quantity * flour_in_recipe

    @property
    def total_water_in_recipe(self) -> float:
        """
        Returns the amount of water in the recipe minues the amount of water in the starter.
        """
        water_in_starter = self._return_amount_of_water_in_starter(ratio=self.starter_ratio)
        unit_value = self._return_unit_value()
        water_in_recipe = (unit_value * self.hydration) - water_in_starter
        return self.quantity * water_in_recipe

    @property
    def total_salt(self) -> float:
        """
        Returns the amount of salt in the recipe based on the unit value calculation and
        the percent of salt in the loaf.
        """
        unit_value = self._return_unit_value()
        salt_in_recipe = unit_value * self.salt
        return self.quantity * salt_in_recipe

    @property
    def total_starter(self) -> float:
        """
        Returns the sum of the amount of flour in starter and the amount of water in starter.
        """
        amount_of_starter_in_recipe = (
            self._return_amount_of_flour_in_starter()
            + self._return_amount_of_water_in_starter(ratio=self.starter_ratio)
        )
        return self.quantity * amount_of_starter_in_recipe


def round_to_nearest_half(number):
    return round(number * 2) / 2


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
    "-y",
    "--starter",
    type=float,
    dest="starter",
    required=True,
    help="percent starter as a portion of fermented flour",
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
    )
    flour = round(dough.total_flour_in_recipe, 2)
    water = round(dough.total_water_in_recipe, 2)
    salt = round(dough.total_salt, 2)
    starter = round(dough.total_starter, 2)

    if not parsed_args.round:
        print(
            f"Number of dough balls: {parsed_args.quantity}\n\nRecipe:\nFlour: "
            f"{flour}g\nWater: {water}g\nSalt: {salt}g\nStarter: {starter}g"
        )
    else:
        flour = round_to_nearest_half(flour)
        water = round_to_nearest_half(water)
        salt = round_to_nearest_half(salt)
        starter = round_to_nearest_half(starter)
        print(
            f"Number of dough balls: {parsed_args.quantity}\n\nRecipe:\nFlour: "
            f"{flour}g\nWater: {water}g\nSalt: {salt}g\nStarter: {starter}g"
        )


if __name__ == "__main__":
    main()
