import data
import sandwich_maker
import cashier

# Create variables from the data module's dictionaries
resources = data.resources
recipes = data.recipes

# Create instances of each class
machine = sandwich_maker.SandwichMaker(resources)
cashier_obj = cashier.Cashier()

machine_on = True

while machine_on:
    # Build the menu prompt dynamically from available recipes
    menu_options = "/".join(recipes.keys())
    choice = input(f"What would you like? ({menu_options}/report/off): ").lower()

    if choice == "off":
        print("Shutting down the Sandwich Maker Machine. Goodbye!")
        machine_on = False

    elif choice == "report":
        # Print current resource levels
        for ingredient, amount in machine.resources.items():
            print(f"{ingredient.capitalize()}: {amount}")

    elif choice in recipes:
        recipe = recipes[choice]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]

        # Check if there are enough resources
        if machine.check_resources(ingredients):
            # Process payment
            coins = cashier_obj.process_coins()
            # Verify transaction and make sandwich if successful
            if cashier_obj.transaction_result(coins, cost):
                machine.make_sandwich(choice, ingredients)

    else:
        print("Sorry, that item is not available. Please choose from the menu.")
