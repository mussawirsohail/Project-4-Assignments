import random

def number_guessing_game(max_number, max_attempts):
    secret_number = random.randint(1, max_number)
    attempts = 0
    previous_guess_diff = None

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts to guess it correctly.\n")

    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > max_number:
                print(f"Please enter a number within the range 1 to {max_number}.")
            elif user_guess == secret_number:
                print(f"\nCongrats! You guessed the number {secret_number} correctly in {attempts} attempts.")
                break
            else:
                current_diff = abs(secret_number - user_guess)
                if previous_guess_diff is not None:
                    if current_diff < previous_guess_diff:
                        print("You're getting warmer!")
                    elif current_diff > previous_guess_diff:
                        print("You're getting colder!")
                    else:
                        print("You're at the same distance as before.")
                else:
                    print("Keep guessing!")

                previous_guess_diff = current_diff
                if attempts == max_attempts:
                    print(f"\nSorry! You've run out of attempts. The correct number was {secret_number}.")
                    
        except ValueError:
            print("That's not a valid number. Please try again.")
number_guessing_game(20, 5)
