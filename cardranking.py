#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:



st.title("Card Ranking Comparison Tool")

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]

pool = pd.DataFrame()
pool.columns = ['Name', 'GIH WR']

# gitview
  
card1 = st.text_input('Card 1')

proc1 = gihwr['Name'].str.contains(card1.title())
proc2 = gihwr[proc1]

st.write(proc2[['Name', 'GIH WR']])

if st.button('Click here to add the previous results to your pool'):
  
  pool = pool + proc2[['Name', 'GIH WR']]
  

color = proc2['Color']

for i in color:
  
  color = i
  
card2 = st.text_input('Card 2')

proc3 = gihwr['Name'].str.contains(card2.title())
proc4 = gihwr[proc3]

st.write(proc4[['Name', 'GIH WR']])

card3 = st.text_input('Card 3')

proc5 = gihwr['Name'].str.contains(card3.title())
proc6 = gihwr[proc5]

st.write(proc6[['Name', 'GIH WR']])

card4 = st.text_input('Card 4')

proc7 = gihwr['Name'].str.contains(card4.title())
proc8 = gihwr[proc7]

st.write(proc8[['Name', 'GIH WR']])


gitview = gitview.replace({'GIH WR': r'%'}, {'GIH WR' : ''}, regex=True)
gitview['GIH WR'] = gitview['GIH WR'].apply(float)

st.write()

supportc = gitview.loc[(gitview['Color'] == color) & (gitview['Rarity'] == 'C') & (gitview['GIH WR'] >= 50)]
supportu = gitview.loc[(gitview['Color'] == color) & (gitview['Rarity'] == 'U') & (gitview['GIH WR'] >= 50)]

col1, col2 = st.columns(2)

with col1:
  
  st.header('Best Common with the same color')
  st.write(supportc[['Name', 'GIH WR']])

with col2:
  
  st.header('Best Uncommon with the same color')
  st.write(supportu[['Name', 'GIH WR']])
  
univsupportc = gitview.loc[(gitview['Rarity'] == 'C') & (gitview['GIH WR'] >= 50)]
univsupportu = gitview.loc[(gitview['Rarity'] == 'U') & (gitview['GIH WR'] >= 50)]


col3, col4 = st.columns(2)

with col3:
  
  st.header('Best Common in any Color')
  st.write(univsupportc[['Name', 'GIH WR']])

with col4:
  
  st.header('Best Uncommon in any Color')
  st.write(univsupportu[['Name', 'GIH WR']])
  
 





