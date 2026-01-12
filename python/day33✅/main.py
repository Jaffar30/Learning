import requests
import datetime
import smtplib
import time

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    return 21 <= iss_lat <= 31 and 45 <= iss_lng <= 55

def is_night():
    parameter = {
        'lat' : 26.066700,
        'lng' : 50.557701,
        'formatted' : 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    now = datetime.datetime.now().hour
    return now >= sunset or now <= sunrise

print(is_night())
print(is_overhead())

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("ahmedmh2209@gmail.com","Password :)")
        connection.sendmail(
            from_addr="ahmedmh2209@gmail.com",
            to_addrs="ahmedmh2209@gmail.com",
            msg="Subject:look up\n\n The ISS above you"
        )
