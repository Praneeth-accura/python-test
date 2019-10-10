import json
from bs4 import BeautifulSoup
import requests

url = 'https://ikman.lk/en/ads?by_paying_member=0&sort=relevance&buy_now=0&query=bmw&page=1'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


def get_objetc_details():
  object_list = []
  for add_list in content.findAll('div', attrs={"class": "container--2uFyv"}):
    list = {
      "title": add_list.find('span', attrs={"class": "title--3yncE"}).text.encode('utf-8'),
      "price": add_list.find('div', attrs={"class": "price--3SnqI color--t0tGX"}).text.encode('utf-8'),
      "short_decription": add_list.find('div', attrs={"class": "description--2-ez3"}).text.encode('utf-8'),
    }
    object_list.append(list)
  return object_list


# with open('data.json', 'w', encoding='utf-8') as f:
#   json.dump(get_objetc_details(), f, ensure_ascii=False, indent=4)