import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

# get the data


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(URL, data=json_data)

    data = r.json()
    print(data)

# get_data()
# post data function

def post_data():
    data = {
        'name': 'bipin',
        'roll': 100,
        'address': 'Pokhara',
        'email': 'bipin@tested.com'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL, data=json_data)
    res = req.json()
    print(res)


post_data()
# update data function
def update_data():
    data = {
        'id':4,
        'name': 'Updates',
        'roll': 222,
        'address': 'New Address',
        'email': 'updatesemail@test.com'
        
    }
    json_data = json.dumps(data)
    req = requests.put(url=URL, data=json_data)
    res = req.json()
    print(res)

# update_data()

# delete function
def delete_data():
    data = {
        'id':1,
        
    }
    json_data = json.dumps(data)
    req = requests.delete(url=URL, data=json_data)
    res = req.json()
    print(res)

# delete_data()
