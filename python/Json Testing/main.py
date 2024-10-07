import json

# A Python dictionary
data = {
"name": "John",
"age": 30,
"city": "New York"
}

# Serialize the dictionary into a JSON formatted string
json_data = json.dumps(data)

# Output the JSON string
# print(json_data)

with open ("python/Json Testing/man.json") as file:
    man_data = json.load(file)

print(man_data)
