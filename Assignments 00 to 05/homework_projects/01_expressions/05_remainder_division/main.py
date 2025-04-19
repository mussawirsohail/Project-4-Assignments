def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    result = dividend // divisor
    remainder = dividend % divisor

    print(f"The result of this division is {result} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
