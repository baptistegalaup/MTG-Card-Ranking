#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Librairies

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# Setup

image = Image.open('mtg___valakut_exploration_by_aenami_de5ispb-fullview.jpg')
st.image(image)

st.title('Card Ranking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2602.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]
  

if 'pool' not in st.session_state:
  
  st.session_state.pool = pd.DataFrame(columns=['Name','GIH WR'])

def concat1():
  
  st.session_state.pool = pd.concat([st.session_state.pool, proc2[['Name', 'GIH WR']]])

def concat2():
  
  st.session_state.pool = pd.concat([st.session_state.pool, proc4[['Name', 'GIH WR']]])
  
def reset():
  
  st.session_state.pool = pd.DataFrame(columns=['Name','GIH WR'])

  
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
  
  st.session_state.pool

  st.button('Click here to reset your pool', on_click=reset)
