def double_numbers(numbers):
    return [number * 2 for number in numbers]

numbers = [3, 6, 6, 12]
numbers = double_numbers(numbers)
print(f"Doubled numbers: {numbers}")
