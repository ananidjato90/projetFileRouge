#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.maisonsdumonde.com/FR/fr/c/meubles-0efb00bec42f8fb7b942b4b76ad5c077'
page = requests.get(url)
print(page)

#commande similaire à la précédentes
page2 = urlopen(url)

html = BeautifulSoup(page.text, 'html.parser')
print("\n", html.find('h1'))

#site = soup.findAll(name = "span", attrs = {"class": "line"})

nomProduit = html.find_all('h2',{'class':'font-weight-normal expand-link name mb-0'})

#print(nomProduit)

produit = []
for elt in nomProduit:
    produit.append(elt.text)

#print("\n", produit[:5])

df = pd.DataFrame(list(produit), columns = ["Nom du produit"])
print(df.head())

