import re

text = "I have 2 apples, 5 bananas and 10 oranges."

numbers = re.findall(r"\d+", text)

print(numbers)