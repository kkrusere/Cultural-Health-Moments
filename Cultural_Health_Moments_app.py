#importing the needed libraries, we will use the pandas dataframe to store the data from Google Trends 
import os
import streamlit as st
import random
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud


import boto3
import pymysql
from sqlalchemy import create_engine, text

#db info

# AWS credentials and region
aws_access_key = st.secrets['aws_access_key']
aws_secret_key = st.secrets['aws_secret_key']
region = st.secrets['region']

# RDS database details
host = st.secrets['db_host']
db_instance_identifier = st.secrets['db_instance_identifier']
username = st.secrets['db_user']
password = st.secrets['db_password']
database_name = st.secrets['db_name']
port = st.secrets['db_port']

#we will have to import TrendReq from PyTrends to request data from Google Trends 
from pytrends.request import TrendReq

###########################################################################################

#hl is the host language, 
#tz is the time zone and 
# retries is the number of retries total/connections/read all represented by one scalar
pytrend = TrendReq(hl = 'en-US', tz = 0, retries=10)


###########################################################################################

st.set_page_config( page_title="Cultural Health Moments App",
                    page_icon= "random",
                    layout="wide"
 )


###########################################################################################
@st.cache_data
def load_data():
    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database_name}")

    try:
        query = f"SELECT * FROM Cultural_Health_Moments_Table"
        df = pd.read_sql(query,engine)

    except Exception as e:
        print(str(e))
    
    check_list = [pytrend.suggestions(keyword=x)[0]['mid'] for x in df["Name_of_HPP"]]
    check_list2 = [pytrend.suggestions(keyword=x)[0]['mid'] for x in df["Chronic_Condition"]]
    return df, check_list, check_list2

#loading the list into a pandas dataframe
data, check_list, check_list2= load_data()


st.dataframe(check_list)