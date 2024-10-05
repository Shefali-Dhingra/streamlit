# General import section
import streamlit as st #streamlit backend

def main(data_obj):
    """Data Preview main

    :param data_obj: DataObject instance
    :type data_obj: __main__.DataObject
    """
    st.header("DATA PREVIEW")
    col1, col2 = st.columns(2)
    col3 = st.columns(2)
    
    with col1:
        st.subheader("Original dataframe")
        st.dataframe(data_obj.df)
        st.write(data_obj.df.shape)
        
    with col2:
        st.subheader("Dataframe description")
        st.dataframe(data_obj.df.describe())
    
    with col3:
        st.subheader("Data types")
        st.dataframe(data_obj.df.dtypes.astype(str))
        

# Main
if __name__ == "__main__":
   main()
