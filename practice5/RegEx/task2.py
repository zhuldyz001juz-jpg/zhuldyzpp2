import re

text = "My name is John. I live in Almaty."

words = re.findall(r"\b[A-Z][a-z]*\b", text)

print(words)