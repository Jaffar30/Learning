import requests
from twilio.rest import Client

api_key = "Not Allow to commit"

sid = "Not Allow to commit"
token = "Not Allow to commit"
weather = {
    'lat' : 26.066700,
    'lon' : 50.557701,      
    'appid' : api_key,
    'cnt' : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather)
response.raise_for_status()
records = response.json()

is_true = False

for rec in records['list']:
    if rec['weather'][0]['id'] < 600:
        is_true = True
# is_true = True 
if is_true:
    client = Client(sid,token)
    msg = client.messages \
        .create(
            body = "Hi Ahmed,\nIt's Going to Rain,\n BECAREFUL GET READY FOR IT",
            from_ = "+12702136976",
            to = "+973 3722 5951"
        )
        