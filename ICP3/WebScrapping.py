import urllib.request
from bs4 import BeautifulSoup
import os

web_url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
wiki_request = urllib.request.urlopen(web_url)
wiki_parse = BeautifulSoup(wiki_request, "html.parser")

web_title = wiki_parse.find('title')

#web_link = wiki_parse.find_all('a', href=True)
for a in wiki_parse.find_all('a', href=True):
    print ("Found the URL:", a['href'])

wiki_table = wiki_parse.find( "table", {"class" : "wikitable sortable plainrowheaders"})

trs = wiki_table.find_all("tr")
for tr in trs:
    #print("tr tsg:",tr)
    td_data=tr.find_all("td")

    for td in td_data:
        print(td.text)
    if tr.find("td"):
         print(tr.find("td").text)
    if tr.find("th"):
         print(tr.find("th").text)

