import re

text = "My email is test@gmail.com"

email = re.findall(r"\w+@\w+\.\w+", text)

print(email)