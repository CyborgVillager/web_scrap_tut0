from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

# Scraping for web server rack
base_url = "https://chicago.craigslist.org/search/sss?query=computer+server&sort=rel"

# Send get http request
page = requests.get(base_url)

# Verify we had a successful get request call
if page.status_code == requests.codes.ok:
    # Obtain the whole page.
    bs = BeautifulSoup(page.text, 'lxml')

# Get all listings on this page

listings = bs.find('div', class_='content').find('ul', class_='rows').find_all('li')

# Hold the data
data = {
    'Name': [],
    'Price': [],
    'Date': [],
}


for computer_listing in listings:

    name = computer_listing.find('a', class_='result-title hdrlnk').text
    if name:
        data['Name'].append(name)
    else:
        data['Name'].append('None')

    price = computer_listing.find('span', class_='result-price').text
    if price:
        data['Price'].append(price)
    else:
        data['Price'].append('None')


    date = computer_listing.find('time', class_='result-date')
    if date:
        data['Date'].append(date)
    else:
        data['Date'].append('None')

# Store data to csv with pandas
df = pd.DataFrame(data, columns=['Name', 'Price','Date'])  # taking in a dict or multi dimensional array. dict keys match with columns param

# change the range from 0-9, to 1-10. df.index is a range
df.index = df.index + 1
print(df)
df.to_csv('craigslist_computer_server_info.csv', sep=',', index=False, encoding='utf-8')


