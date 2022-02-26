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

st.write(proc3.head(5))

card2 = st.text_input('Card 2')

proc4 = gitview['Name'].str.contains(card1.title())
proc5 = gitview[proc1]
proc6 = proc5[['Name', 'GIH WR']]

st.write(proc6.head(5))

card3 = st.text_input('Card 3')

proc7 = gitview['Name'].str.contains(card1.title())
proc8 = gitview[proc1]
proc9 = proc8[['Name', 'GIH WR']]

st.write(proc9.head(5))

card4 = st.text_input('Card 5')

proc10 = gitview['Name'].str.contains(card1.title())
proc11 = gitview[proc10]
proc12 = proc11[['Name', 'GIH WR']]

st.write(proc12.head(5))

card5 = st.text_input('Card 5')

proc13 = gitview['Name'].str.contains(card1.title())
proc14 = gitview[proc13]
proc15 = proc14[['Name', 'GIH WR']]

st.write(proc15.head(5))

card6 = st.text_input('Card 6')

proc16 = gitview['Name'].str.contains(card1.title())
proc17 = gitview[proc16]
proc18 = proc17[['Name', 'GIH WR']]

st.write(proc18.head(5))
