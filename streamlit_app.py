# General import section
import pandas as pd #to work with dataframes
import streamlit as st #streamlit backend
from io import StringIO #to read data files as .csv correctly
import os #to work with files

# Streamlit main page configuration
st.set_page_config(
                    page_icon="💻",
                    layout="wide",
                    initial_sidebar_state="expanded",
                    menu_items=None)

# App import
import Welcome
import Data_Preview
# import Data_Preparation
# import Smoothing_and_Filtering
# import Regression
# import Classification

dt_obj.df = pd.read_csv('data/Imports_Exports_Dataset.csv')
            ## Add 3001 sample
dt_obj.filesize = dt_obj.df.size

with st.sidebar:
  st.title('💻Dashboard💻') 
  menu = ['Data Preview', 'Data Preparation']
  navigation = st.sidebar.selectbox(label="Select menu", options=menu)

        # Runs 'Data Preview' app
if navigation == 'Data_Preview':
  with st.container():
    Data_Preview.data_preview(dt_obj)

        # Runs 'Data Preparation' app
if navigation == 'Data Preparation':
  with st.container():
    Data_Preparation.data_prep(dt_obj)
      
      # Initial welcome page when there is no file selected
else:
  Welcome.welcome()
