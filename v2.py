#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Librairies

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from st_aggrid import AgGrid

# Setup

#image = Image.open('mtg___valakut_exploration_by_aenami_de5ispb-fullview.jpg')
#st.image(image, width=1200)

st.title('Card Ranking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2802.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]
                                                        
gihwr['GIHWRMOD'] = gihwr['GIH WR']
gihwr = gihwr.replace({'GIHWRMOD':r'%'}, {'GIHWRMOD' : ''}, regex=True)
gihwr['GIHWRMOD'] = gihwr['GIHWRMOD'].apply(float)    

if 'pool' not in st.session_state:
  
  st.session_state.pool = pd.DataFrame(columns=['Name','GIH WR'])
  
st.session_state.pool['GIHWRMOD'] = st.session_state.pool['GIH WR']
st.session_state.pool = st.session_state.pool.replace({'GIHWRMOD':r'%'}, {'GIHWRMOD' : ''}, regex=True)
st.session_state.pool['GIHWRMOD'] = st.session_state.pool['GIHWRMOD'].apply(float)  
  
if 'winrate' not in st.session_state:
  
  st.session_state.winrate = 0

def concat1():
  
  st.session_state.pool = pd.concat([st.session_state.pool, proc2[['Name', 'GIH WR']]])

def concat2():
  
  st.session_state.pool = pd.concat([st.session_state.pool, proc4[['Name', 'GIH WR']]])
  
def reset():
  
  st.session_state.pool = pd.DataFrame(columns=['Name','GIH WR'])
  
def increment():
  
  if st.session_state.winrate ==0:
    
    
    st.session_state.winrate = float(proc2['GIHWRMOD'])
                                          
  else:
                                        
    st.session_state.winrate = (st.session_state.winrate + proc2['GIHWRMOD']) / 2

  
# Body

col1, col2 = st.columns(2)

with col1:

  card1 = st.text_input('Card 1')

  proc1 = gihwr['Name'].str.contains(card1.title())
  proc2 = gihwr[proc1]

  st.write(proc2[['Name', 'GIH WR']])

  st.button('Click here to add the previous results to your pool', on_click = concat1, key=1)


  card2 = st.text_input('Card 2')

  proc3 = gihwr['Name'].str.contains(card2.title())
  proc4 = gihwr[proc3]

  st.write(proc4[['Name', 'GIH WR']])
  
  

  st.button('Click here to add the previous results to your pool', on_click = concat2, key=2)

    
with col2:
 
  st.write('Your Pool')
  
  st.session_state.pool[['Name', 'GIH WR']]
     
  st.session_state.winrate  =  st.session_state.pool['GIHWRMOD'].mean()
  
  st.write('The winrate of your pool is about ', round(st.session_state.winrate, 2),'%') 
                                                                                                                                          
  if st.button('Click here to reset your pool'):
    
    st.selectbox('Are you sure?', ('No', 'Yes'), on_change=reset)
 

st.header('Top 10 Cards by Rarity')

col3,col4,col5:

with col3:
  
  st.write('Mythic/Rare')
  
  st.write(gihwr[['Name', 'GIHWRMOD']].head(10))
