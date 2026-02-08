import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


app_id = 'app_c8c1167c49a34daabc4ef52d'
app_key = 'nix_live_rPEm83jZ1oMIGPa7na0dpDN54B9KsduC'

url_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
url_sheet = 'https://api.sheety.co/a915b0c78ee4d2aa068707542720d773/sectionDay38/workouts'

text = input("Tell me which exercises you did: ")

header = {
'x-app-id': app_id,
'x-app-key': app_key
}
basic = HTTPBasicAuth('ahmed2309' , 'AhmedAhmed123')
parameter = {
    "query": text,
    "gender": 'male',
    "weight_kg": 64.5,
    "height_cm": 173,
    "age": 23
}

response = requests.post(url_endpoint, json=parameter, headers=header)
records = response.json()

for record in records['exercises']:
        inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": record["name"].title(),
            "duration": record["duration_min"],
            "calories": record["nf_calories"]
            }
        }
        sheet_response = requests.post(url_sheet, json=inputs,auth=basic)
        print(sheet_response.text)