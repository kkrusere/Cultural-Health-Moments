#importing the needed libraries, we will use the pandas dataframe to store the data from Google Trends 
import pytrends
import streamlit as st
import time
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import widgets, Layout
import plotly.express as px
from IPython import display
from IPython.core.display import display, HTML
from wordcloud import WordCloud
#we will have to import TrendReq from PyTrends to request data from Google Trends 
from pytrends.request import TrendReq


def load_data():
    df = pd.read_csv('Cultural_Health Moments_Data.csv')
    return df

#loading the list into a pandas dataframe
data = load_data()

data['Important_Date_1'] =  pd.to_datetime(data['Important_Date_1'])
data['Important_Date_2'] =  pd.to_datetime(data['Important_Date_2'])

st.markdown(" ## ***Cultural Health Moments:*** ")
st.markdown("A Search Analysis During Times of Heightened Awareness To Identify Potential Interception Points With Digital Health Consumers.")

st.markdown("### ***Project Contributors:***")
st.markdown("Sirui Yang, Kuzi Rusere, Ye An & Umair Shaikh")

st.markdown("* ***Vision:*** Understanding how cultural health moments"
            "impact health consumers’ digital search behavior may provide insight into potential" 
            "interception points relating to disease-state awareness, education, symptoms, diagnosis, and/or treatment.")

st.markdown("* ***Issue:*** During high-profile health moments "
            "(ex. – the cancer-related deaths of Chadwick Boseman and Eddie Van Halen, "
            "or the cancer diagnosis of Jimmy Carter or Rush Limbaugh) digital health consumers’ "
            "initial search queries are typically surface-level search (ex. – scandal, wealth, career highlights, spouse, etc.), "
            "but that search behavior shifts to awareness, signs, symptoms, and introspection over time. Understanding that time "
            "horizon – when the shift occurs and what common topical trends exist – may provide opportunities to engage by leveraging "
            "naturally occurring awareness and search.")

st.markdown("* ***Method:*** Examination of publicly available search data as related to high-profile disease state diagnosis and/or deaths. ")

st.markdown("For the data collection in this project we are going to use Google Trend specifically PyTrends. "
            "Google Trends => is a website by Google that analyzes the popularity of top search queries in Google Search across various regions and languages. "
            "The website uses graphs to compare the search volume of different queries over time. "
            "PyTrends inturn is a Python library/module/API that Allows simple interface for automating downloading of reports from Google Trends")