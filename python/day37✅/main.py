import requests
from datetime import datetime

pixela_endpoit = "https://pixe.la/v1/users"

user = {
    'token' : 
    'username' : 
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=pixela_endpoit , json=user)
# print(response.text)

graph_url = f"{pixela_endpoit}/ahmed2309/graphs"
graph={
    'id' : 'graph1',
    'name' : 'Reading Graph',
    'unit' : 'page',
    'type' : 'int',
    'color' : 'kuro'
}
header = {
    'X-USER-TOKEN' : 
}
# response = requests.post(url=graph_url , json=graph , headers=header)
# print(response.text)

today = datetime.now()

create_endpoint = f"{pixela_endpoit}/ahmed2309/graphs/graph1"
data = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : input("How many pages you read today? "),
}
response = requests.post(url=create_endpoint , json=data , headers=header)
print(response.text)

# update_endpoint = f"{pixela_endpoit}/ahmed2309/graphs/graph1/{today.strftime('%Y%m%d')}"

# new_data = {
#     'quantity' : '50'
# }
# response = requests.put(url=update_endpoint , json=new_data,headers=header)
# print(response.text)

# delete_endpoint = f"{pixela_endpoit}/ahmed2309/graphs/graph1/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=header)
# print(response.text)