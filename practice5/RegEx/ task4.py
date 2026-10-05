import re

text = "Call me: +77001234567"

phone = re.findall(r"\+7\d{10}", text)

print(phone)