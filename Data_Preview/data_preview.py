# General import section
import streamlit as st #streamlit backend

def main(df):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA PREVIEW")
    col1, col2 = st.columns(2)
    col3 = st.columns(1)
    
    with col1:
        st.subheader("Original dataframe")
        st.dataframe(df)
        st.write(df.shape)
        
    with col2:
        st.subheader("Dataframe description")
        st.dataframe(df.describe())
    
    with col3:
        st.subheader("Data types")
        st.dataframe(df.dtypes.astype(str))

# Main
if __name__ == "__main__":
   main()
