#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


st.title("Card Ranking Comparison Tool")

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]

# gitview

card1 = st.text_input('Card 1')

proc1 = gihwr['Name'].str.contains(card1.title())

proc2 = gihwr[proc1]

st.write(proc2)

color = proc2['Color']

def num(df):
  
  dfnum = df['GIH WR'].replace('%', '')
  dfnum['GIH WR'] = int(dfnum['GIH WR'])
  
  return dfnum
  

# gitview.loc[(gitview['Color'] == color) & (gitview['Rarity'] == 'Common' & (gitview['GIH WR'] >= 60%)
