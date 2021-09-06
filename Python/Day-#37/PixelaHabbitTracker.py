import requests
from requests.api import request

# refer pixela.txt more details about creating the user
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "nandisha"
TOKEN = "thisissecret"

# Create your user account
user_parameters = {
    "token": TOKEN, 
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# {"message":"Success. Let's visit https://pixe.la/@nandisha , it is your profile page!","isSuccess":true}

# Create a graph definition
#Call /v1/users/<username>/graphs by HTTP POST.
graph_api_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
graph_id = "graph1"

graphs_parameters = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_api_endpoint, json=graphs_parameters) # {"message":"User `nandisha` does not exist or the token is wrong.","isSuccess":false}
# response = requests.post(url=graph_api_endpoint, json=graphs_parameters, headers=headers) 

# ---------------------4. Post value to the graph--------------------------------#
# Call /v1/users/<username>/graphs/<graphID> by HTTP POST.
graphs_post_api = f"{graph_api_endpoint}/{graph_id}"

# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

# date	string	[required] The date on which the quantity is to be recorded. It is specified in yyyyMMdd format.
# quantity	string	[required] Specify the quantity to be registered on the specified date.

from datetime import datetime
date = datetime.now().strftime("%Y%m%d")
# date = "20210905"

post_my_data = {
    "date" : date,
    "quantity" : "9.5"
}


# response = requests.post(url=graphs_post_api, json=post_my_data, headers=headers) # {"message":"Success.","isSuccess":true}
# print(response.text)
# --------------------------------------------------------------------------------#

# ------------------------------PUT METHOD---------------------------------------#
# $ curl -X PUT https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret' -d '{"quantity":"7","optionalData":"{\"key\":\"value\"}"}'
# {"message":"Success.","isSuccess":true}

put_api_endpoint = f"{graphs_post_api}/{date}"

put_data = {
    "quantity" : "14" 
}

# response = requests.put(url=put_api_endpoint, json=put_data, headers=headers)
# print(response.text)
# --------------------------------------------------------------------------------#

# ------------------------------DELETE METHOD---------------------------------------#
# $ curl -X DELETE https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret'
# {"message":"Success.","isSuccess":true}

delete_api_endpoint = f"{graphs_post_api}/{date}"

response = requests.delete(url=delete_api_endpoint, json=put_data, headers=headers)
print(response.text)
# --------------------------------------------------------------------------------#
