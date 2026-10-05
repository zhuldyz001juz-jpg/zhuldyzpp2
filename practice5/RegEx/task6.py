import re

text = """
Apple 2.50
Milk 1.80
Bread 1.20
Total 5.50
"""

prices = re.findall(r"\d+\.\d{2}", text)

print(prices)