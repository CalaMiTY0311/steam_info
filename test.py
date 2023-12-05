import bs4 as bs
import urllib.request
import xmltodict as xml
from pprint import pprint
#opening a connection 
my_url = urllib.request.urlopen('https://store.steampowered.com/search/?specials=1&os=win').read()


#turning the html into a beautifulsoup object
soup = bs.BeautifulSoup(my_url, 'lxml')
def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

data_discounts = (soup.find_all('div', {'class':'col search_discount responsive_secondrow'}))
data_body = (soup.find_all('span', {'class':'title'}))
pprint (data_body)