
import pandas as pd 
import streamlit as st
import streamlit_func as func
import streamlit_info as info

data = pd.read_csv(info.data_path,sep=';')

st.sidebar.title('MENU')
st.sidebar.file_uploader(
        label='User Data',
        type='csv'
    )

menu = st.sidebar.selectbox('Selection Menu',('Home','Graph','Filter'))

if menu == 'Home':

    func.main_selector()

    func.expander()

    func.echo_data(data)

if menu == 'Graph':

    func.graph(data)

if menu == 'Filter':

    data = func.filter_options(data)
    func.graph(data)
