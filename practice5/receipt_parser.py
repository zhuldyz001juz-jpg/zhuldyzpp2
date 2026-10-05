import re

with open("raw.txt", "r") as file:
    text = file.read()

print(text)

# Находим цены
prices = re.findall(r"\d+\.\d{2}", text)

print("Prices:")
for price in prices:
    print(price)