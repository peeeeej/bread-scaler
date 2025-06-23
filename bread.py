import argparse
class Loaf():
    def __init__(self, quantity=int, weight=int|float, hydration=int|float, salt=int|float, starter=int|float):
        self.quantity = quantity
        self.weight = weight
        self.hydration = hydration
        self.salt = salt
        self.starter = starter

    def return_unit_value(self) -> float:
        """
        Needed to determine downstream ingredient amounts based on weight of the loaf, 
        hydration and the amount of salt
        """
        unit_value = self.weight / (100 + (self.hydration + self.salt))
        return round(unit_value, 2)
    
    def return_starter_multiplier(self) -> float:
        """
        Needed to determine how much of the flour and water in the recipe is coming 
        from the starter.
        """
        starter_multipler = self.starter * .01
        return starter_multipler
    
    def return_amount_of_water_and_flour_in_starter(self) -> float:
        """
        Determining the amount of flour and water in starter. We're assuming a starter with 
        equal parts water and flour. Returns an amount that we'll need to double (e.g. if it 
        returns 85, that means 85g water and 85g flour.)
        """
        unit_value = self.return_unit_value()
        starter_multiplier = self.return_starter_multiplier()
        amount_in_starter = (unit_value * 100) * starter_multiplier
        return amount_in_starter

    def return_flour_in_recipe(self) -> float:
        """
        Returns the amount of flour in the recipe minus the amount of flour in the starter.
        """
        flour_in_starter = self.return_amount_of_water_and_flour_in_starter()
        unit_value = self.return_unit_value()
        flour_in_recipe = (unit_value * 100) - flour_in_starter
        return round((self.quantity * flour_in_recipe), 2)
    
    def return_water_in_recipe(self) -> float:
        """
        Returns the amount of water in the recipe minues the amount of water in the starter.
        """
        water_in_starter = self.return_amount_of_water_and_flour_in_starter()
        unit_value = self.return_unit_value()
        water_in_recipe = (unit_value * self.hydration) - water_in_starter
        return round((self.quantity * water_in_recipe), 2)
    
    def return_salt_in_recipe(self) -> float:
        """
        Returns the amount of salt in the recipe based on the unit value calculation and 
        the percent of salt in the loaf.
        """
        unit_value = self.return_unit_value()
        salt_in_recipe = unit_value * self.salt
        return round((self.quantity * salt_in_recipe), 2)
    
    def return_starter_in_recipe(self) -> float:
        """
        I'm assuming equal amounts of water and flour in the starter.
        """
        half_amount_of_starter = self.return_amount_of_water_and_flour_in_starter()
        amount_of_starter_in_recipe = half_amount_of_starter * 2
        return round((self.quantity * amount_of_starter_in_recipe), 2)


argParser = argparse.ArgumentParser()
argParser.add_argument("-q", "--quantity", type=int, dest="quantity", required=False, help="number of doughballs or loaves")
argParser.add_argument("-d", "--dough-weight", type=float, dest="weight", required=True, help="weight per dough ball or loaf")
argParser.add_argument("-w", "--water", type=float, dest="hydration", required=True, help="percent hydration")
argParser.add_argument("-s", "--salt", type=float, dest="salt", required=True, help="percent salt")
argParser.add_argument("-y", "--starter", type=float, dest="starter", required=True, help="percent starter as a portion of fermented flour")

if __name__ == "__main__":
    parsed_args = argParser.parse_args()
    if not parsed_args.quantity:
        quantity = 1
    else:
        quantity = parsed_args.quantity
    weight = parsed_args.weight
    hydration = parsed_args.hydration
    salt = parsed_args.salt
    starter = parsed_args.starter

    bread = Loaf(quantity=quantity, weight=weight, hydration=hydration, salt=salt, starter=starter)
    flour = bread.return_flour_in_recipe()
    water = bread.return_water_in_recipe()
    salt = bread.return_salt_in_recipe()
    starter = bread.return_starter_in_recipe()
    print(f"Number of dough balls: {quantity}\n\nRecipe:\nFlour: {flour}g\nWater: {water}g\nSalt: {salt}g\nStarter: {starter}g")

# TODO: list specific flour amounts e.g. rye, wheat, etc