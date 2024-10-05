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

# Data object class
class DataObject():
    """
    Data object class holds a dataframe and its byte size.
    """
    def __init__(self, df=None, filesize=None):
      """The constructor for DataObject class

      :param df: pandas dataframe object, defaults to None
      :type df: pandas.core.frame.DataFrame, optional
      :param filesize: byte size of pandas dataframe, defaults to None
      :type filesize: numpy.int32, optional
      """
      self.df = df
      self.filesize = filesize


# Interface class        
class Interface():
    """
    Interface class contains a file picker and a side bar. It also handles the import of a data object.
    """
    def __init__(self):
      """The constructor for Interface class.
      """
      pass
    
    def side_bar(cls, dt_obj):
      """Sidebar configuration and file picker

      :param dt_obj: pandas dataframe object
      :type dt_obj: pandas.core.frame.DataFrame
      """
      # Accepts .csv and .data
      filename = st.sidebar.file_uploader("Upload a data file", type=(["csv", "data"]))                   
      if filename is not None: #file uploader selected a file      
        try: #most datasets can be read using standard 'read_csv'                                                                                           
            dt_obj.df = pd.read_csv(filename, sep=';|,', decimal=',', engine='python')                                                                     
            dt_obj.filesize = dt_obj.df.size
        except: #due to a different encoding some datafiles require additional processing
            filename.seek(0)
            filename = filename.read()
            filename = str(filename,'utf-8')
            filename = StringIO(filename)
            #now the standard 'read_csv' should work
            dt_obj.df = pd.read_csv(filename, sep=';', decimal=',', index_col = False)
            ## Add 3001 sample
            dt_obj.filesize = dt_obj.df.size
      
        # Side bar navigation menu with a select box
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

def main():
  """
  Main and its Streamlit configuration
  """

  # Creating an instance of the original dataframe data object                   
  data_main = DataObject()
  # Creating an instance of the main interface
  interface = Interface()
  interface.side_bar(data_main)


# Run Main
if __name__ == '__main__':
  main()
