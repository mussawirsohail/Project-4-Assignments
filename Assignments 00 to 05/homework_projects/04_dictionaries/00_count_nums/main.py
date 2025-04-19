number_counts = {}

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        number = int(user_input)
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1
    except ValueError:
        print("Please enter a valid number.")

for number, count in number_counts.items():
    print(f"{number} appears {count} times.")
