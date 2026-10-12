from functools import reduce

numbers = [1, 2, 3, 4, 5]

# len: count elements
print("Length:", len(numbers))

# sum: add all numbers
print("Sum:", sum(numbers))

# min and max
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# map: multiply every number by 2
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)

# filter: keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce: calculate the total
total = reduce(lambda x, y: x + y, numbers)
print("Reduce total:", total)

# sorted: sort numbers
print("Sorted:", sorted([5, 2, 4, 1, 3]))

# Type checking and conversion
number = "25"
print("Type:", type(number))
print("Integer:", int(number))
print("Float:", float(number))
print("String:", str(100))
print("Boolean:", bool(1))