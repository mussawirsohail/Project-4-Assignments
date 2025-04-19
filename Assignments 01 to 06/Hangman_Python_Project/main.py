import random
import string

words = [
    "python", "variable", "function", "loop", "string", "integer", "boolean", "syntax",
    "operator", "condition", "debug", "compile", "execute", "parameter", "argument",
    "recursion", "exception", "library", "module", "package", "framework", "object",
    "class", "method", "inheritance", "encapsulation", "polymorphism", "abstraction",
    "algorithm", "array", "list", "tuple", "dictionary", "set", "stack", "queue",
    "binary", "search", "sort", "merge", "quick", "bubble", "hashmap", "graph",
    "tree", "node", "edge", "vertex", "matrix", "pointer", "memory", "compile",
    "interpreter", "constant", "keyword", "input", "output", "debugger", "source",
    "index", "element", "command", "argument", "file", "stream", "network", "socket",
    "thread", "process", "server", "client", "request", "response", "router",
    "protocol", "secure", "encrypt", "decrypt", "access", "control", "admin",
    "user", "login", "logout", "session", "cookie", "token", "backend", "frontend",
    "database", "schema", "query", "table", "column", "row", "relation", "join",
    "model", "view", "controller", "render", "route", "url", "form", "submit",
    "validate", "error", "exception", "try", "catch", "finally", "assert", "test",
    "mock", "unit", "integration", "deploy", "build", "branch", "commit", "merge",
    "push", "pull", "clone", "repository", "version", "history", "debug", "log",
    "config", "setup", "install", "uninstall", "update", "upgrade", "virtual",
    "environment", "shell", "terminal", "command", "prompt", "execute", "script",
    "automation", "schedule", "event", "trigger", "listener", "handler", "object",
    "attribute", "property", "instance", "static", "private", "public", "protected"
]

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. You have already used these letters: {', '.join(used_letters)}")

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_guess = input("Guess a letter: ").upper()

        if len(user_guess) != 1 or user_guess not in alphabets:
            print("Please enter a single valid letter.")
            continue

        if user_guess in used_letters:
            print("You already guessed that letter. Try again.")
        else:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print(f"Good guess! {user_guess} is in the word.")
            else:
                lives -= 1
                print(f"Sorry, {user_guess} is not in the word.")

    if lives == 0:
        print(f"Sorry, you lost. The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing!")
hangman()
