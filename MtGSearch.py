from bs4 import BeautifulSoup as bs
import requests
import selenium
import urllib.requests

cardName = input("Card Name")
cardName = cardName.replace(' ', '-').lower()
cardName = cardName.replace("'", '%27').lower()

print(cardName)

input()
 
