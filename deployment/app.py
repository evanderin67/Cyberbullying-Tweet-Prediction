import streamlit as st
import eda
import prediction

# Set Config dan icon
st.set_page_config(
        page_title='Churn Prediction',
        layout='wide',
        )

# Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Membuat navigasi
st.sidebar.markdown("# Evan Derin Ihsanudin - RMT-FTDS-17")
navigation = st.sidebar.selectbox('Pilih Halaman (Tweet Prediction/EDA): ', ('Tweet Prediction','Exploratory Data Analysis'))
st.sidebar.image("https://imgur.com/MmPULSL.png", use_column_width=True)

# Run modul dengan if else
if navigation == 'Tweet Prediction' :
    prediction.run()
else :
    eda.run()