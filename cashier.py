class Cashier:
    """Handles all payment processing and transaction logic."""

    def process_coins(self):
        """Prompt the user to insert coins and calculate the total amount entered.

        Returns:
            float: The total monetary value of the coins inserted.
        """
        print("Please insert coins.")
        total = 0
        total += int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Check whether the inserted amount covers the sandwich cost and process the transaction.

        Args:
            coins (float): The total amount of money inserted by the user.
            cost (float): The price of the requested sandwich.

        Returns:
            bool: True if the transaction is successful, False if payment is insufficient.
        """
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
