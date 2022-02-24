#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


st.title("Card Ranking Comparison Tool")

overview = pd.read_csv(r"C:\Users\Baptiste\Documents\Projets autour de MTG\Projet card ranking\intro.csv", sep=",")

overview
