from bs4 import BeautifulSoup



'''
is a Python library for pulling data out of HTML and XML files. 
It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree
'''
import requests  # allow you to requests web pages to get html code
import lxml  # allow you to read html files in a certain format

base_url = 'https://en.wikipedia.org/wiki/World_Soccer_(magazine)'

# when requesting url, its called a GET request place in the base_url
# Send get http request
page = requests.get(base_url)
# print(type(page))

# If you get 200 it means a successul get request
# print(page)
# print(page.status_code)

# Ensure get request is successful
if page.status_code == requests.codes.ok:

    # Get entire webpage in beautifulsoup format
    # print(page.text)
    Beautiful_Soup = BeautifulSoup(page.text, 'lxml')
    # Find something you are speacifi in the html
    # shave off unness info by using .prettify()
    # print(Beautiful_Soup.find('table', class_='multicol'))

    # this just look for all
    all_players_list = Beautiful_Soup.find('table', class_='multicol' ).find('ul').find_all('li')
    last_ten_players = all_players_list[-10:]
    print(last_ten_players)