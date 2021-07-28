import pandas as pd
import streamlit as st
import streamlit_info as info 

def main_selector(image = info.tittle_image):

    @st.cache(persist=False)
    def csv_loader():
        st.balloons()

    st.title('CARGATRON')

    st.image(image)#, caption='Image footing')

def expander():

    with st.beta_expander('Description'):

        st.write('A must for people with electric cars in Madrid and surroundings')

def echo_data(data):

    with st.echo(code_location='above'):

        st.write('Code that opens the data used')
        st.write(data)

def graph(data):

    df_map = data.iloc[:,-2:]

    df_map.columns=['longitude','lat']

    st.map(df_map)

    df_district = data[['DISTRITO','Nº CARGADORES']]

    df_bar_chart = df_district.groupby('DISTRITO')['Nº CARGADORES'].sum()

    df_bar_chart = pd.DataFrame(df_bar_chart)

    st.bar_chart(df_bar_chart)

    df_operador = data[['OPERADOR','Nº CARGADORES']]

    df_bar_chart = df_operador.groupby('OPERADOR')['Nº CARGADORES'].sum()

    df_bar_chart = pd.DataFrame(df_bar_chart)

    st.bar_chart(df_bar_chart)

def filter_options(data):

    filter_district = st.sidebar.selectbox('District',(data.DISTRITO.unique()))
    district_check = st.sidebar.checkbox('Filter by District?')
    filter_operator = st.sidebar.selectbox('Operator',(data.OPERADOR.unique()))
    operator_check = st.sidebar.checkbox('Filter by Operator?')
    filter_size = st.sidebar.select_slider('Size',options=[1,2,3,4,5,6,7,8,9,10],value = (1,10))
    size_check = st.sidebar.checkbox('Filter by Size?')
    
    if district_check:

        data= data.loc[data['DISTRITO'] == filter_district, :]

    if operator_check:

        data = data.loc[data['OPERADOR'] == filter_operator, :]

    if size_check:
        min_size = filter_size[0]
        max_size = filter_size[1]
        data = data.loc[(data['Nº CARGADORES'] >= min_size) & (data['Nº CARGADORES'] <= max_size), :]

    return data