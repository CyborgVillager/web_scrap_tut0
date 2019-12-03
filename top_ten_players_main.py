from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"

# Send get http request
page = requests.get(base_url)

# Verify we had a successful get request webpage call
if page.status_code == requests.codes.ok:

  # Get the whole webpage in beautiful soup format
  bs = BeautifulSoup(page.text, 'lxml')

# Find something you spcify in the html
list_of_all_players = bs.find('table', class_='multicol').find('ul').find_all('li')
last_ten_players = list_of_all_players[-10:]

# Will hold our data
data = {
  'Year': [],
  'Country': [],
  'Player': [],
  'Team': []
}

# Scrape all 10 polayers in the top 10 list
for list_item in last_ten_players:

  # Get the year and save it in the data dictionary
  year = list_item.find('span').previousSibling.split()[0]
  if year:
    data['Year'].append(year)
  else:
    data['Year'].append('none')

  # Get the country and save it in the data dictionary
  country = list_item.find('a')['title']
  if country:
    data['Country'].append(country)
  else:
    data['Country'].append('none')

  # Get the player name and save it in the data dictionary
  player = list_item.find_all('a')[1].text
  if player:
    data['Player'].append(player)
  else:
    data['Player'].append('none')

  # Get the team name and save it in the data dictionary
  team = list_item.find_all('a')[2].text
  if team:
    data['Team'].append(team)
  else:
    data['Team'].append('none')


table = pd.DataFrame(data, columns=['Year', 'Country', 'Player', 'Team'])
table.index = table.index + 1
print(table)
table.to_csv('players_of_the_year.csv', sep=',', index=False, encoding='utf-8')
