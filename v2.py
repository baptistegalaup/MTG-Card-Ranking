#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Librairies

import streamlit as st
import pandas as pd
import numpy as np

# Setup

st.title('Card Ranking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2602.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]
  
pool = pd.DataFrame(columns=['Name','GIH WR'])

if 'pool' not in st.session_state:
  
  st.session_state.pool = pd.DataFrame(columns=['Name','GIH WR'])

def concat1():
  
  st.session_state.pool = pd.concat([st.session_state.pool, proc2[['Name', 'GIH WR']]])

# Body

col1, col2 = st.columns(2)

with col1:

  card1 = st.text_input('Card 1')

  proc1 = gihwr['Name'].str.contains(card1.title())
  proc2 = gihwr[proc1]

  st.write(proc2[['Name', 'GIH WR']])

  st.button('Click here to add the previous results to your pool', on_click = concat1, key=1)


#    pool = pd.concat([pool, proc2[['Name', 'GIH WR']]])


  card2 = st.text_input('Card 2')

  proc3 = gihwr['Name'].str.contains(card2.title())
  proc4 = gihwr[proc3]

  st.write(proc4[['Name', 'GIH WR']])

  if st.button('Click here to add the previous results to your pool', key=2):

    pool = pd.concat([pool, proc4[['Name', 'GIH WR']]])

    
with col2:
 
  st.write('Your Pool')
  
  st.session_state.pool

#  if st.button('Click here to reset your pool'):
    
#    pool = pd.DataFrame(columns=['Name','GIH WR'])
