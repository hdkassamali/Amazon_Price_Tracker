import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

WILSON_BASKETBALL_URL = "https://www.amazon.com/WILSON-NCAA-Indoor-Game-Basketball/dp/B09KS6P52Z/ref=sr_1_1_mod_primary_new?crid=3TOAL8A1XTQU1&keywords=wilson%2Bevo&qid=1679358144&s=home-garden&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=wilson%2Bevo%2B%2Cgarden%2C141&sr=1-1-catcorr&th=1&psc=1"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("MY_PASS")

BUY_PRICE = 150

http_headers = {
  "User-Agent": "Defined",
  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4"
}

response = requests.get(url=WILSON_BASKETBALL_URL, headers=http_headers)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")

price_tag = soup.find(name="span", class_="a-offscreen").get_text()
price = float(price_tag.split("$")[1].strip())

listing = soup.find(name="span", id="productTitle").get_text().strip()

if price < BUY_PRICE:
  with smtplib.SMTP("smtp.gmail.com", port=587) as email:
    email.starttls()
    email.login(user=MY_EMAIL, password=MY_PASS)
    email.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=MY_EMAIL,
      msg=f"Subject: Amazon Price Alert!\n\n{listing} is now ${price}\n{WILSON_BASKETBALL_URL}"
    )









