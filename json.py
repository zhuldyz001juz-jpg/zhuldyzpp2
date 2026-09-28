import json

data = '{"name": "Malia", "age": 21}'

person = json.loads(data)

print(person)

print(person["name"])


json.dumps(data) #Python → JSON
json.loads(data) #JSON → Python