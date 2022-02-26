#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

st.title('Card Ranking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")

card1 = st.text_input('Card 1')

proc1 = gitview['Name'].str.contains(card1.title())
proc2 = gitview[proc1]
proc3 = proc2[['Name', 'GIH WR']]

proc3.head(5)
