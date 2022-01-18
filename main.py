import requests

url = 'https://hookb.in/G90xNbkeW2HE2xPP2o0O'

data = {
    "name": "John"
}

r = requests.post(url, verify=False, json=data)
