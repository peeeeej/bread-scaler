class Loaf():
    def __init__(self, weight=int|float, hydration=int|float, salt=int|float, starter=int|float):
        self.weight = weight
        self.hydration = hydration
        self.salt = salt
        self.starter = starter

    def return_unit_value(self):
        """
        Needed to determine downstream ingredient amounts based on weight of the loaf, 
        hydration and the amount of salt
        """
        unit_value = self.weight / (100+(self.hydration + self.salt))
        return unit_value
    
    def return_starter_multiplier(self):
        """
        Needed to determine how much of the flour and water in the recipe is coming 
        from the starter.
        """
        starter_multipler = self.starter * .01
        return starter_multipler
    
    def return_amount_of_water_and_flour_in_starter(self):
        """
        Determining the amount of flour and water in starter. We're assuming a starter with 
        equal parts water and flour. Returns an amount that we'll need to double (e.g. if it 
        returns 85, that means 85g water and 85g flour.)
        """
        unit_value = self.return_unit_value()
        starter_multiplier = self.return_starter_multiplier()
        amount_in_starter = (unit_value * 100) * starter_multiplier
        return amount_in_starter

    def return_flour_in_recipe(self):
        """
        Returns the amount of flour in the recipe minus the amount of flour in the starter.
        """
        flour_in_starter = self.return_amount_of_water_and_flour_in_starter()
        unit_value = self.return_unit_value()
        flour_in_recipe = (unit_value * 100) - flour_in_starter
        return round(flour_in_recipe, 2)
    
    def return_water_in_recipe(self):
        """
        Returns the amount of water in the recipe minues the amount of water in the starter.
        """
        water_in_starter = self.return_amount_of_water_and_flour_in_starter()
        unit_value = self.return_unit_value()
        water_in_recipe = (unit_value * 100) - water_in_starter
        return round(water_in_recipe, 2)
    
    def return_salt_in_recipe(self):
        """
        Returns the amount of salt in the recipe based on the unit value calculation and 
        the percent of salt in the loaf.
        """
        unit_value = self.return_unit_value()
        salt_in_recipe = unit_value * self.salt
        return round(salt_in_recipe, 2)
    
    def return_starter_in_recipe(self):
        """
        I'm assuming equal amounts of water and flour in the starter.
        """
        half_amount_of_starter = self.return_amount_of_water_and_flour_in_starter()
        amount_of_starter_in_recipe = half_amount_of_starter * 2
        return round(amount_of_starter_in_recipe, 2)


if __name__ == "__main__":
    bread = Loaf(weight=875, hydration=72, salt=2.2, starter=17)
    flour = bread.return_flour_in_recipe()
    water = bread.return_water_in_recipe()
    salt = bread.return_salt_in_recipe()
    starter = bread.return_starter_in_recipe()
    print(f"Flour: {flour}g\nWater: {water}g\nSalt: {salt}g\nStarter: {starter}g")