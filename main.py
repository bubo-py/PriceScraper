import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/currencies/bitcoin/" # set url
p = requests.get(url) # get that url by requests 

soup = BeautifulSoup(p.content, "html.parser") # set url above as a page content

result = soup.find() # find all the things in soup variable(not much clear yet)
# find more specific things by calling 'div' with a class
results = result.find_all("div", class_="cmc-details-panel-price jta9t4-0 fcilTk")

for x in results: # iterate for all things in the results variable(in html 'div)
    value = x.find('span', class_='cmc-details-panel-price__price') # take data from THAT 'span'
    change = x.find('span', class_='cmc--change-positive cmc-details-panel-price__price-change')
    if None in (value, change):
        continue # sometimes values can NOT show up 
                    # and that statement is to help script to not crash if so
print(f"BTC is now worth {value.text}, with the{change.text} rate of 24h change.")
#formated via 'f strings'