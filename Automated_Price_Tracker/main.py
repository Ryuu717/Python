import os
from dotenv import load_dotenv
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=psdc_3117954011_t2_B07W55DDFB?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
}
load_dotenv("/Users/Ryuuuu/PycharmProjects/Automated_Price_Tracker/.env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


response = requests.get(url, headers=header)
# soup = BeautifulSoup(response.text, "html.parser")
soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())


price = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay").getText().split("$")[2]
# print(price)
price_as_float = float(price)
print(price_as_float)

title = soup.find(id="productTitle").getText().strip()
print(title)


BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8')
        )