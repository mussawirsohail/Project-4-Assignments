fruit_prices = {
    "apple": 1.5,
    "durian": 50.0,
    "jackfruit": 80.0,
    "kiwi": 1.0,
    "rambutan": 1.5,
    "mango": 5.0
}

total_cost = 0.0
for fruit, price in fruit_prices.items():
    while True:
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
            if quantity < 0:
                print("Please enter a non-negative number.")
                continue
            total_cost += quantity * price
            break
        except ValueError:
            print("Please enter a valid number.")

print(f"\nYour total is ${total_cost}")
