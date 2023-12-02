import time

import requests as r
from datetime import datetime
import smtplib

MY_EMAIL = 'atifshaikh1996@gmail.com'
MY_PASSWORD = 'nvfjodqtjjprucit'


MY_LAT = 18.520430
MY_LONG = 73.856743

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def iss_overhead():
    response = r.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    position = (latitude, longitude)

    if MY_LAT - 5 <= position <= MY_LAT + 5 and MY_LONG <= position <= MY_LONG:
        return True


def is_night():
    response = r.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour

    if sunset <= current_time <= sunrise:
        return True

while True:
    if iss_overhead() and is_night():
        time.sleep(120)
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg='Hello, this is automated email')
        connection.close()





