import json

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
#     "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
# }
#
# response = requests.get(
#     "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
#     headers=header)
#
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
#
# all_link_elements = soup.select(".list-card-top a")
# all_link_elements = soup.find_all(name="a", class_="list-card-link")
# print(len(all_link_elements))
#
# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https://www.zillow.com{href}")
#     else:
#         all_links.append(href)

# all_address_elements = soup.select(".list-card-info address")
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
#
# all_price_elements = soup.select(".list-card-heading")
# all_prices = []
# for element in all_price_elements:
#     # Get the prices. Single and multiple listings have different tag & class structures
#     try:
#         # Price with only one listing
#         price = element.select(".list-card-price")[0].contents[0]
#     except IndexError:
#         print('Multiple listings for the card')
#         # Price with multiple listings
#         price = element.select(".list-card-details li")[0].contents[0]
#     finally:
#         all_prices.append(price)
#
#
# Create Spreadsheet using Google Form
# chrome_driver_path = "/Users/Ryuuuu/Development/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# for n in range(len(all_links)):
#     driver.get("https://docs.google.com/forms/d/e/1FAIpQLSed53QKYxkXZ3Y3yxdJnrztXn9S_4G40THP5O7ndBUBICFRoQ/viewform?usp=sf_link")
#
#     time.sleep(2)
#     address = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element_by_xpath(
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
#
#     address.send_keys(all_addresses[n])
#     price.send_keys(all_prices[n])
#     link.send_keys(all_links[n])
#     submit_button.click()


#-------------------------------------------------------------------------------#
#Another Method(because I couldn't get all page data)
#-------------------------------------------------------------------------------#

zillow_url = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8"
}

r = requests.get(zillow_url, headers=header)
zillow_results = r.text
soup = BeautifulSoup(zillow_results, "html.parser")

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
        .contents[0]
        .strip("!<>-")
)


# get house links
house_links = [
    result["detailUrl"]
    for result in data["cat1"]["searchResults"]["listResults"]
]

# amend house_links to have all proper URLS
house_links = [
    link.replace(link, "https://www.zillow.com" + link)
    if not link.startswith("http")
    else link
    for link in house_links
]
print(f"Houses: {len(house_links)}")
# Get address
house_address = [
    result["address"]
    for result in data["cat1"]["searchResults"]["listResults"]
]

# Get price
house_rent = [
    int(result["units"][0]["price"].strip("$").replace(",", "").strip("+"))
    if "units" in result
    else result["unformattedPrice"]
    for result in data["cat1"]["searchResults"]["listResults"]
]


# Create Spreadsheet using Google Form
# Substitute your own path here 👇
chrome_driver_path = "/Users/Ryuuuu/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(house_links)):
    # Substitute your own Google Form URL here 👇
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSed53QKYxkXZ3Y3yxdJnrztXn9S_4G40THP5O7ndBUBICFRoQ/viewform?usp=sf_link")

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(house_address[n])
    price.send_keys(house_rent[n])
    link.send_keys(house_links[n])
    submit_button.click()