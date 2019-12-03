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


# Will hold the data

def get_player_info():
    data = {
        'Year': [],
        'Country': [],
        'Player': [],
        'Team': [],
    }
# Scrape the site for top 10 players
    for list_items in last_ten_players:

        # .previousSibling -> property returns the previous node of the specified node, in the same tree level
        # get the year
        year = list_items.find('span').previousSibling.split()[0]
        # if no year exist place in dictionary None
        if year:
            data['Year'].append(year)
        else:
            data['Year'].append('None')

    # get the country name
        country = list_items.find('a')['title']
        # if no country exist place in dictionary None
        if country:
            data['Country'].append(country)
        else:
            data['Country'].append('None')

    # get the player name by finding all 'a' tags
    # .text just gives you the name of the player
        player_name = list_items.find_all('a')[1].text
        # if no player name exist place in dictionary None
        if player_name:
            data['Player'].append(player_name)
        else:
            data['Player'].append('None')

    # team
        team_name = list_items.find_all('a')[2].text
        # if no team name exist place in dictionary None
        if team_name:
            data['Team'].append(team_name)
        else:
            data['Team'].append('None')

    #pd.DataFrame create a db
    panda_get_info = pd.DataFrame(data, columns=['Year', 'Country', 'Player', 'Team'])
    print(panda_get_info)
    panda_get_info.to_csv('top_players_of_the_year.csv', sep=',', index=False, encoding='utf-8')

def main():
    get_player_info()


main()
