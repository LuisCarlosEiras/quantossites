#!/usr/bin/env python
# coding: utf-8

import streamlit as st

from googletrans import Translator
translator = Translator()

st.title('Quantos sites e servidores tem a internet?')

import requests
from requests import get
from bs4 import BeautifulSoup


url = "https://news.netcraft.com/archives/category/web-server-survey"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
container = soup.find("div",attrs={'class': 'post__content'})
paragraph = container.find("p")
for p in container.find_all("p", limit = 1):  
    p.text
    
result=translator.translate(p.text, dest='pt') 
st.write(result.text)

st.write("""*Fonte*: Netcraft""")







