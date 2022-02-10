import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient    #for Pythonanywhere

from dotenv import load_dotenv

load_dotenv("/Users/Ryuuuu/PycharmProjects/Send_SMS/.env")
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("AUTH_TOKEN")
# api_key = os.environ.get("OWM_API_KEY")
# account_sid = os.environ.get("account_sid")
# auth_token = os.environ.get("AUTH_TOKEN")

DUMMY_NUMBER = os.getenv("DUMMY_NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": "40.826530",
    "lon": "140.754715",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# print(weather_data)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    #How to get Twilio from proxy server(Pythonanywhere)
    # https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    # message = client.messages \
    #     .create(
    #     body="It's going to rain today. Remember to bring an ☔️",
    #     from_=DUMMY_NUMBER,
    #     to=MY_NUMBER
    # )
    # print(message.status)

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_= DUMMY_NUMBER,
        to = MY_NUMBER
    )
    print(message.status)
