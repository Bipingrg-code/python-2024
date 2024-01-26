import requests
import json

URL = 'http://127.0.0.1:8000/studetails/'
POST_URL = 'http://127.0.0.1:8000/stucreate/'
UPDATE_URL = 'http://127.0.0.1:8000/stuupdate/'
DELETE_URL = 'http://127.0.0.1:8000/studelete/'
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
        'name': 'testing',
        'roll': 201,
        'address': 'Memory',
        'email': 'python1@tested.com'
    }
    json_data = json.dumps(data)
    req = requests.post(url=POST_URL, data=json_data)
    res = req.json()
    print(res)


# post_data()
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
    req = requests.put(url=UPDATE_URL, data=json_data)
    res = req.json()
    print(res)

# update_data()

# delete function
def delete_data():
    data = {
        'id':1,
        
    }
    json_data = json.dumps(data)
    req = requests.delete(url=DELETE_URL, data=json_data)
    res = req.json()
    print(res)

delete_data()
