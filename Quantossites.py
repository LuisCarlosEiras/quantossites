#!/usr/bin/env python
# coding: utf-8

# https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group

import gc
gc.collect()

import streamlit as st

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

import importlib
import googletrans
importlib.reload(googletrans)

from googletrans import Translator
# translator = Translator()

st.write("""*Tradução do googletrans*:""") 
result=Translator().translate(p.text, dest = 'pt').text
st.write(result) 
st.write("""*Fonte*: Netcraft""")

# s = Translator().translate(text='Hello my friend', dest='es').text






