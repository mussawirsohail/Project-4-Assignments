MAX_LENGTH = 3 

def shorten(lst):
    """Remove elements from the end of the list until it's MAX_LENGTH long."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main():
    num_elements = int(input("How many elements do you want to enter? "))
    items = []
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        items.append(element)

    print("Original list:", items)
    shorten(items)
    print("Final list:", items)

if __name__ == "__main__":
    main()
