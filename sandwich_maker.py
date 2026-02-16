class SandwichMaker:
    """Handles all sandwich-making operations including resource checking and sandwich assembly."""

    def __init__(self, resources):
        """Initialize the SandwichMaker with a dictionary of available resources.

        Args:
            resources (dict): A dictionary of ingredient names mapped to their available quantities.
        """
        self.resources = resources

    def check_resources(self, ingredients):
        """Check whether there are sufficient resources to make the requested sandwich.

        Args:
            ingredients (dict): Required ingredients and their quantities for the sandwich.

        Returns:
            bool: True if all resources are sufficient, False otherwise.
        """
        for item, amount in ingredients.items():
            if amount > 0 and self.resources.get(item, 0) < amount:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_name, ingredients):
        """Deduct ingredients from resources and confirm the sandwich is being made.

        Args:
            sandwich_name (str): The name of the sandwich to make.
            ingredients (dict): The ingredients and quantities to deduct.
        """
        for item, amount in ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {sandwich_name}. Enjoy!")
