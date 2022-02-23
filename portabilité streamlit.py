#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


st.title("Card Ranking Comparison for the MTG NEO set")

st.write("version de st =>", st.__version__)
st.write("version de pd =>", pd.__version__)
st.write("version de sns =>", sns.__version__)
st.write("version de plt =>", matplotlib.__version__)

