def play_mad_libs():
    print("\n🎭 Welcome to the *MAD LIBS* Adventure Generator! 🎭")
    print("Get ready to enter some silly words to create your very own wacky story!\n")

    adj1 = input("Give me an adjective: ")
    noun1 = input("Now a noun: ")
    adj2 = input("Another adjective: ")
    noun2 = input("Another noun: ")
    adj3 = input("One more adjective: ")
    noun3 = input("Another noun, please: ")
    verb1 = input("A verb: ")
    verb2 = input("Another verb: ")
    adj4 = input("Adjective again: ")
    noun4 = input("Yet another noun: ")
    verb3 = input("Another verb: ")
    adj5 = input("Adjective: ")
    noun5 = input("Noun again: ")
    verb4 = input("One more verb: ")
    adj6 = input("Final adjective: ")

    mad_lib = f"""
    ~~~~~~~~~~~~~~~~ The Unexpected Journey ~~~~~~~~~~~~~~~~

    Once upon a time, a {adj1} {noun1} was wandering through a {adj2} {noun2},
    in search of a legendary {adj3} {noun3}.

    With a sudden urge, it decided to {verb1} and then {verb2} without a second thought.

    Out of nowhere, a {adj4} {noun4} popped up and {verb3} like nobody was watching!

    Terrified but giggling, the {adj5} {noun5} {verb4} away into the sunset,
    swearing never to return to that {adj6} place again.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    print(mad_lib)

    replay = input("Do you want to create another silly story? (yes/no): ").lower()
    if replay == 'yes':
        play_mad_libs()
    else:
        print("\nThanks for playing! Stay silly 😄")


play_mad_libs()
