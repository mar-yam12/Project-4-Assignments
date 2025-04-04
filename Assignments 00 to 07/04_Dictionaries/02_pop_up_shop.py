def main():
    # Define the price list for each fruit
    fruit_prices = {
        "apple": 2.5,
        "durian": 5.0,
        "jackfruit": 3.0,
        "kiwi": 1.5,
        "rambutan": 4.0,
        "mango": 2.0
    }

    total_cost = 0  # Initialize the total cost

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        # Ask the user how many of each fruit they want
        quantity = int(input(f"\033[1;3mHow many ({fruit}) do you want?: \033[0m"))
        # Add the cost of this fruit to the total cost
        total_cost += quantity * price

    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
