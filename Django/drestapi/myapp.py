import requests
import json 
URL = 'http://localhost:8000/stucreate/'

data = {
    'id': 4,
    'name': 'Third party test',
    'roll': 101,
    'address': 'testing'
}

json_data = json.dumps(data)

req = requests.post(URL,data=json_data)

res_data = req.json()
print(res_data)