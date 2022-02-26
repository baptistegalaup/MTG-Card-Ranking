#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

st.title('Card Rankking Comparison Tool V2')

gitview = pd.read_csv('https://raw.githubusercontent.com/baptistegalaup/MTG-Card-Ranking/main/log2302.csv', sep=",")
