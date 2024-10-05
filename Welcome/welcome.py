import streamlit as st
import os

def main():
    """Welcome main
    """    
    st.header("Streamlit Dashboard - Home Page")
    st.write("""
             Please Upload a DataSet to be analysed
             """)
    st.subheader("Project Contents")
    st.markdown("""
                1. **Home Page:** This is where you currently are!
                2. **Data Description:**  You can have a look at your dataset in general and spot some correlations between the features
                3. **Data Preparation:** Drop and/or rename single/multiple columns, don't forget to submit changes
                """)  
    st.info("The experience from the workflow is the best when all the pages are navigated in sequence!")
    st.subheader("This Project is made by Shefali Dhingra (055043) for The Data Visualisation Dashboard Project, under the Subject Data Exploration and Visualisation using Python (DEVP")
