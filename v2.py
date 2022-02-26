#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

st.title('Card Ranking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR', 'Color']]


card1 = st.text_input('Card 1')

proc1 = gihwr['Name'].str.contains(card1.title())
proc2 = gihwr[proc1]

st.write(proc2[['Name', 'GIH WR']])


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
