#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


st.title("Card Ranking Comparison Tool")

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")
gihwr = gitview[['Name', 'GIH WR']

# gitview

card1 = st.text_input('Card 1')

proc1 = gitview['Name'].str.contains(card1.title())

proc2 = gitview[proc1]

st.write(proc2)
