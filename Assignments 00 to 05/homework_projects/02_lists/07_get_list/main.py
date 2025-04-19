def main():
    values = []

    while True:
        value = input("Enter a value: ")
        if value == "4":
            break
        values.append(value)

    print("Here's the list:", values)

if __name__ == "__main__":
    main()
