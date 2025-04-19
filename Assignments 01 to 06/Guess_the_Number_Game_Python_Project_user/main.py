import random

def computer_guess(max_number, max_attempts=10):
    low = 1
    high = max_number
    feedback = ''
    attempts = 0
    
    print(f"\nThink of a number between 1 and {max_number}.")
    print("The computer will try to guess it!\n")
    print("Give feedback: ")
    print("   - 'L' if the guess is too Low")
    print("   - 'H' if the guess is too High")
    print("   - 'C' if the guess is Correct\n")

    while feedback != 'c' and attempts < max_attempts:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 

        feedback = input(f"Is {guess} too Low (L), too High (H), or Correct (C)? ").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'c':
            print(f"\nYay! The computer guessed your number {guess} correctly in {attempts + 1} attempts!")
            break
        else:
            print("Invalid input. Please enter 'L', 'H', or 'C'.")

        attempts += 1
        
        if attempts == max_attempts:
            print(f"\nOh no! The computer couldn't guess your number within {max_attempts} attempts. Better luck next time!")
            break

computer_guess(10)
