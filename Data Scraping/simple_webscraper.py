from typing import Type
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from copy import deepcopy
from tqdm import tqdm
import json
import pandas as pd


options = Options()
options.headless = True
options.add_argument("window-size=1920,1200")
driver = webdriver.Chrome(options=options)


def save_html(html, path):
    with open(path, "wb") as f:
        f.write(html)


def open_html(path):
    with open(path, "rb") as f:
        return f.read()


# Requests
r = requests.get(
    "https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B2%5D=2&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title="
)
print(r.status_code)
soup = bs4.BeautifulSoup(r.content, "html.parser")
# select returns a list
# td is a data cell, tbody is the table with tr representing each row
rows = soup.select("tbody tr")

# Uses selenium to get the agreeance text
driver.get(
    "https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B2%5D=2&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title="
)

agreeance = driver.find_elements_by_xpath('//span[@class="hidden-xs"]')


data = []
count = 0

for row in rows:
    d = dict()

    d["name"] = row.select_one(".source-title").getText()
    d["allsides_page"] = "https://www.allsides.com" + row.select_one(
        ".source-title a"
    ).get("href")
    d["bias"] = (
        row.select_one(".views-field-field-bias-image a").get("href").split("/")[-1]
    )
    d["agree"] = int(row.select_one(".rate-details .agree").getText())
    d["disagree"] = int(row.select_one(".rate-details .disagree").getText())
    d["agree_ratio"] = d["agree"] / d["disagree"]
    d["agreeance_text"] = agreeance[count].text

    count = count + 1
    data.append(d)


print(data)


# for d in tqdm(data):
#     r = requests.get(d["allsides_page"])
#     soup = bs4.BeautifulSoup(r.content, "html.parser")

#     try:
#         website = soup.select_one(".dynamic-grid a").get("href")
#         d["website"] = website
#     except AttributeError:
#         pass
#     sleep(10)


with open("allsides.json", "w") as f:
    json.dump(data, f)


df = pd.read_json(open("allsides.json", "r"))
df.set_index("name", inplace=True)
df.head()
