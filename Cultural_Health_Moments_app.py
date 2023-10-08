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

###########################################################################################


thelist = list(data['Name_of_HPP'] + " with "+ data['Chronic_Condition'])


dict_mapper = dict()
for i, n in enumerate(thelist):
    dict_mapper[n] = i


col1, col2, col3 = st.columns((.1,1,.1))

with col1:
    st.write("")

with col2:
    st.markdown(" <h1 style='text-align: center;'>Cultural Health Moments:</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><i><b>A Search Analysis During "
                "Times of Heightened Awareness To Identify Potential Interception "
                "Points With Digital Health Consumers.</b></i></p>", unsafe_allow_html=True)
    st.markdown(" <center><img src='https://github.com/kkrusere/Cultural-Health-Moments/blob/main/Assets/DigitalHealth.jpg?raw=1' width=600/></center>", unsafe_allow_html=True)
    

    

with col3:
    st.write("")

st.markdown("### ***Project Contributors:***")
st.markdown("Kuzi Rusere")



row0_space1, row0_1, row0_space2, row0_2, row0_space3 = st.columns((.1, 1, .1, 1, .1))

with row0_1:
    st.subheader("**Vision:**")
    st.markdown("Understanding how cultural health moments impact health consumers’ digital search behavior, "
                "and if this provides insight into potential interception points relating to disease-state awareness, "
                "education, symptoms, diagnosis, and/or treatment.")

with row0_2:
    st.subheader("**Issue:**")
    st.markdown("During high-profile health moments (ex. – the cancer-related deaths of Chadwick Boseman "
                "and Eddie Van Halen, or the cancer diagnosis of Jimmy Carter or Rush Limbaugh) digital health consumers’ "
                "initial search queries are typically surface-level search (ex. – scandal, wealth, career highlights, spouse, etc.), "
                "but the search behavior shifts to awareness, signs, symptoms, and introspection over time. Understanding the time horizon "
                "when the shift occurs and what common topical trends exist may provide opportunities to engage by leveraging naturally "
                "occurring awareness and search.")

st.markdown("---")

row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.columns((.1, 1, .1, 1, .1))

with row1_1:
    st.subheader("**Methodology:**")
    st.markdown("Examination of publicly available search data as related to high-profile disease state diagnosis and/or deaths. ")

with row1_2:
    st.markdown("The Project made use of the Google Search Trends via PyTrends (which is an unofficial Google Trends API). "
                "Google Trends => is a tool by Google that analyzes the popularity (demand, interest overtime) of top search queries in "
                "Google Search across various regions, subjects, and languages. The website uses graphs to compare the search volume of different "
                "queries overtime. PyTrends inturn is a Python library/module/API that Allows a simple interface for automated downloading "
                "of reports from Google Trends.")

st.markdown("---")

st.markdown("You can either use our list of High Profile People, Chronic Condition and Date or you can enter the infomation yourself?")

row2_space1, row2_1, row2_space2, row2_2, row2_space3 = st.columns((.1, 1, .1, 1, .1))

with row2_1:
    route = st.radio( "Please choose one:", ('Use Availabe List', 'Enter Myself'))
    if route == 'Use Availabe List':
        choice = st.selectbox("Availabe List: ", thelist)
        x = 0
    else:
        x = 1
        try:
            name = st.text_input("Enter Name: ", "",key="1")
            condition = st.text_input("Enter Chronic Condition:", "",key="2")
            date = st.text_input("Enter Date: ", "yyyy/mm/dd",key="3")
            Date1 = str(datetime.datetime.strptime(date,"%Y/%m/%d").date())
            check = st.checkbox("Have Another Date")
            if check:
                date2 = st.text_input("Enter Date: ", "yyyy/mm/dd",key="4")
                Date2 = str(datetime.datetime.strptime(date2,"%Y/%m/%d").date())
            
        except ValueError:
            st.warning("Please Make Sure the Date in in the format yyyy/mm/dd, click submit if it's correct")

