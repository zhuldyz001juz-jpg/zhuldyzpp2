import re

text = "Today is 05.10.2026. Tomorrow is 06.10.2026."

dates = re.findall(r"\d{2}\.\d{2}\.\d{4}", text)

print(dates)