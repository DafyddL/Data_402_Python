import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}
print(type(car_data))
# json.dumps() --> turn python dict into string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# json.dump() --> Converts a dict to a str AND puts it in a file
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)
