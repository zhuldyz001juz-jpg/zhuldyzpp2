def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def double_numbers(numbers):
    return [number * 2 for number in numbers]


print(calculate_average([10, 20, 30]))
print(double_numbers([1, 2, 3]))