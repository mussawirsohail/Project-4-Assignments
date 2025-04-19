phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"No contact found for '{name}'.")

    elif choice == "3":
        if phonebook:
            print("\nAll Contacts:")
            for name, phone in phonebook.items():
                print(f"{name}: {phone}")
        else:
            print("Phonebook is empty.")

    elif choice == "4":
        print("Exiting phonebook.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
