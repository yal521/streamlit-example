#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 05:03:08 2023

@author: yangliu
"""

import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv("new_df.csv")

# Display the dataset in a Streamlit app
st.write("My Dataset", data)