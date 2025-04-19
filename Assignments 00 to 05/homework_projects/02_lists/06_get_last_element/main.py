def get_last_element(lst):
    """Print the last element of the list."""
    print(lst[-1])

def main():
    num_elements = int(input("How many elements do you want to add to the list? "))
    
    user_list = []

    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    get_last_element(user_list)

if __name__ == "__main__":
    main()
