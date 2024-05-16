import requests
import json



json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

for entry in post_multi_req.json()['result']:
    print(entry['result']['admin_county'])

print(post_multi_req.json()['result'][0]['result'].keys())
