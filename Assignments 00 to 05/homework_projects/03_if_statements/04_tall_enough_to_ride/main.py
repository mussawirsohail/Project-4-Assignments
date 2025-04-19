def tall_enough():
    MIN_HEIGHT = 50 
    attempts = 0     

    while attempts < 2:
        height_input = input("How tall are you? ")
        height = float(height_input)

        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

        attempts += 1 
    
    print("Goodbye!")

tall_enough()
