def get_first_element(lst):
    """Print the first element of the list."""
    print(lst[0])

def main():
    user_list = []
    num_elements = int(input("How many elements do you want to add to the list? "))
    for i in range(num_elements):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element) 
    get_first_element(user_list)

if __name__ == "__main__":
    main()
