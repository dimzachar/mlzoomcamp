import requests

url = "http://localhost:9696/predict"

customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
respose = requests.post(url, json=customer).json()

print(respose)

