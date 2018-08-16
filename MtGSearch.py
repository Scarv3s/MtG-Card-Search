from bs4 import BeautifulSoup as bs
import requests
import selenium

cardName = input("Card Name: ")
cardName = cardName.replace(' ', '+').lower()
cardName = cardName.replace("'", '%27').lower()
cardName = cardName.replace(",", '%2C')

print(cardName)

input()
