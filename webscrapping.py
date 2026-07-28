#import section
import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")
#print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

names=soup.find_all('div',class_='_nZIRY7')
print(names)