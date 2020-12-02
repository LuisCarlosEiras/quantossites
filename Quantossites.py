#!/usr/bin/env python
# coding: utf-8

import gc
gc.collect()

import streamlit as st

from translate import Translator
translator = Translator(to_lang = "pt")

st.title('Quantos sites e servidores têm a internet?')

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
    
st.write("""*Tradução do googletrans*:""") 
result=translator.translate(p.text) 
st.write(result)
st.write("""*Fonte*: Netcraft""")







