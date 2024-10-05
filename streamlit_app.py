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


df = pd.read_csv('data/Imports_Exports_Dataset.csv')
filesize = df.size

with st.sidebar:
  st.title('💻Dashboard💻') 
  menu = ['HomePage','Data Preview']
  navigation = st.sidebar.selectbox(label="Select menu", options=menu)

        # Runs 'Data Preview' app
if navigation == 'Welcome Page':
  with st.container():
    Welcome_Page.welcome()


if navigation == 'Data_Preview':
  with st.container():
    Data_Preview.data_preview(df)
      
      # Initial welcome page when there is no file selected
else:
  Welcome.welcome()
