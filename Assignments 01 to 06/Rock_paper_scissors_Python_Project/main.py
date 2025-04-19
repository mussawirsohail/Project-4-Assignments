import random

def play_game():
    print("\n🎮 Welcome to Rock, Paper, Scissors!")
    print("Make your move:")
    print("  🪨 'r' for Rock")
    print("  📄 'p' for Paper")
    print("  ✂️  's' for Scissors")

    choices = {'r': '🪨 Rock', 'p': '📄 Paper', 's': '✂️ Scissors'}
    user = input("\nYour choice (r/p/s): ").lower()

    if user not in choices:
        print("\n❌ Invalid choice! Please enter 'r', 'p', or 's'.")
        return

    computer = random.choice(['r', 'p', 's'])

    print(f"\n🧍 You chose: {choices[user]}")
    print(f"🤖 Computer chose: {choices[computer]}")

    if user == computer:
        print("⚖️ It's a Tie!")
    elif is_win(user, computer):
        print("🎉 You Won!")
    else:
        print("💻 Computer Won!")

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play():
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("\n👋 Thanks for playing! Goodbye!\n")
            break
play()
