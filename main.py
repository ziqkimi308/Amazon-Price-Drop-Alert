"""
********************************************************************************
* Project Name:  Amazon Price Drop Alert
* Description:   This project scrapes product price data from Amazon using BeautifulSoup. If the price of a specific item drops below a predefined threshold, an email is automatically sent to notify the user. This can help track deals and discounts for items on Amazon.
* Author:        ziqkimi308
* Created:       2024-12-30
* Updated:       2024-12-30
* Version:       1.0
********************************************************************************
"""

import requests
from bs4 import BeautifulSoup
import smtplib
# import lxml # The lxml library is used internally by BeautifulSoup as the parser, no need import

# CONTANTS
# --- CHANGE YOUR AMAZON PRODUCT WEB URL HERE ---
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# --- CHANGE YOUR EMAIL DETAILS HERE ---
MY_EMAIL = ""
MY_PASSWORD = "" # Use app pasword, not regular email password
TARGET_EMAIL = ""

# Scrapping Amazon using BeautifulSoup
AMAZON_HEADERS = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
	"Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(AMAZON_URL, headers=AMAZON_HEADERS)
amazon_web_text = response.text

soup = BeautifulSoup(amazon_web_text, "lxml")

# Use find to find first occurence that class and use split to remove dollar sign
price = soup.find("span", class_="a-offscreen").getText().split("$")[1]
price_float = float(price)
print("Scrapped price...")

# Scrap the title
title = soup.find("span", id="productTitle").getText()
print("Scrapped title...")

# Setup to send email if price drops
# --- CHANGE YOUR PRICE LIMIT HERE ---
PRICE_LIMIT = 200
if price_float < PRICE_LIMIT:
	connection = smtplib.SMTP("smtp.gmail.com", 587)
	connection.starttls()
	connection.login(MY_EMAIL, MY_PASSWORD)
	connection.sendmail(
		from_addr=MY_EMAIL,
		to_addrs=TARGET_EMAIL,
		msg=f"Subject: Amazon Price Alert!\n\nItem: {title}\nPrice Now: {price}\nLink: {AMAZON_URL}".encode("utf-8")
	)
# The sendmail method expects a message in byte format, and .encode("utf-8") is used to convert the string (text) into bytes using the UTF-8 encoding.
print("Email was set!")