import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.reddit.com/r/funny/comments/ebxvjv/if_this_isnt_the_single_most_target_thing_i_have/")

soup = BeautifulSoup(response.text, 'lxml')

hr = soup.find_all('h1')
for i in hr:
    print(i.get_text())

print(hr)
