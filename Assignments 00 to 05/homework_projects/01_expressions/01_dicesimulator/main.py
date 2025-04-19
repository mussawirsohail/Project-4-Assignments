import random

def roll_dice():
    die1 = random.randint(1, 10)
    die2 = random.randint(1, 20)
    print(f"Die 1: {die1}, Die 2: {die2}")

def main():
    print("Rolling dice... Round 1:")
    roll_dice()

    print("\nRolling dice... Round 2:")
    roll_dice()

    print("\nRolling dice... Round 3:")
    roll_dice()

if __name__ == "__main__":
    main()