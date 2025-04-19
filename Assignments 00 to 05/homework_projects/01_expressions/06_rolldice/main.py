import random

def roll_dice():
    die1 = random.randint(1, 50)
    die2 = random.randint(1, 50)
    
    print(f"Die 1: {die1}, Die 2: {die2}")
    total = die1 + die2
    print(f"Total: {total}")

def main():
    roll_dice()

if __name__ == "__main__":
    main()
