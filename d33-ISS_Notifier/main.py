import requests
from datetime import datetime
import smtplib
import time

def send_mail():
    EMAIL = <MYMAIL>
    PASSWORD = <PASSWORD>
    TO = <FROM>

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(
            to_addrs=TO,
            from_addr=EMAIL,
            msg="LOOK OVERHEAD FOR THE ISS \n\n Check the ISS the your city NOW"
        )

def is_iss_in_my_city():
    url_ISS = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url_ISS)
    data = response.json()

    lat_ISS = float(data["iss_position"]["latitude"])
    long_ISS = float(data["iss_position"]["longitude"])
    return (lat_ISS - 5 <= MY_LAT <= lat_ISS + 5) and (long_ISS - 5 <= MY_LGN <= long_ISS + 5)

def is_is_dark():

    weather_URL = "https://api.sunrise-sunset.org/json"

    param = {
        "lat": MY_LAT,
        "lng": MY_LGN,
        "formatted": 0
    }

    weather_res = requests.get(weather_URL, params=param)
    weather_data = weather_res.json()

    sunrise = int(weather_data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(weather_data["results"]["sunset"].split('T')[1].split(":")[0])
    time_now = datetime.now().hour

    return time_now <= sunrise or time_now >= sunset


MY_LAT = 43.709422
MY_LGN = -1.055488

while True:
    time.sleepl(60)
    if is_iss_in_my_city() and is_is_dark():
        send_mail()



