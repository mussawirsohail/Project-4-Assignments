def add_three_copies(my_list, data):
    """Add three copies of data to my_list."""
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    # Get user input
    message = input("Enter a message to copy: ")

    # Initialize an empty list
    my_list = []

    # Display the list before calling add_three_copies
    print("List before:", my_list)

    # Call the function to add three copies of the message
    add_three_copies(my_list, message)

    # Display the list after calling add_three_copies
    print("List after:", my_list)

if __name__ == "__main__":
    main()
