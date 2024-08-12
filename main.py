import requests
from datetime import datetime

PIXELA_TOKEN = "yourtoken"
PIXELA_USERNAME = "yourusername"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
        "id": GRAPH_ID,
        "name": "Reading Graph",
        "unit": "Pages",
        "type": "int",
        "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/graph1"

today = datetime.now()
pixela_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11"
}

# response = requests.post(url=pixela_creation_endpoint, json=pixela_creation_config, headers=headers)
# print(response.text)


pixela_update_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}//{today.strftime("%Y%m%d")}"

pixela_update_config = {
    "quantity": "5"
}

# response = requests.put(url=pixela_update_endpoint, json=pixela_update_config, headers=headers)
# print(response.text)


pixela_delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=pixela_update_endpoint, headers=headers)
# print(response.text)