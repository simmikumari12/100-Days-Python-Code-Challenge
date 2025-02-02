import requests
import random
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"

unique_value = random.randint(1,100)

response = requests.get(url, headers={"user-agent": f"simmi{unique_value}"})

html = response.content

soup = BeautifulSoup(html, 'html.parser')

a_tags = soup.find_all("a", class_="entry-title-link")

print("\n")

for a_tag in a_tags:
    print(f"{a_tag.get_text()}")
print("\n")

print(list(map(lambda a_tag: a_tag.get_text() ,a_tags)))
print("\n")

"""
Use map to take the a-tags that we have here in line 15 and put them into a list with just title in there
"""


