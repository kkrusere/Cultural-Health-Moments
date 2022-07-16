#importing the needed libraries, we will use the pandas dataframe to store the data from Google Trends 

import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

#we will have to import TrendReq from PyTrends to request data from Google Trends 
from pytrends.request import TrendReq

temp_data = pd.read_csv("http://goodcsv.com/wp-content/uploads/2020/08/us-states-territories.csv", encoding= 'unicode_escape')
temp_data = temp_data[["Name","Abbreviation"]]
temp_data["Name"] = temp_data["Name"].str.strip()
temp_data["Abbreviation"] = temp_data["Abbreviation"].str.strip()
temp_data["Name"] = [name.replace( "[E]", "" ) for name in temp_data["Name"]]
code = dict(zip(temp_data['Name'], temp_data['Abbreviation']))

st.set_option('deprecation.showPyplotGlobalUse', False)


name = ''
condition = ''
Date = ''
Date1 = ''
Date2 = ''
x = 0

st.set_page_config( page_title="Cultural Health Moments App",
                    page_icon= "random",
                    layout="wide"
 )

#hl is the host language, 
#tz is the time zone and 
# retries is the number of retries total/connections/read all represented by one scalar
pytrend = TrendReq(hl = 'en-US', tz = 0, retries=10)

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('Cultural-Health-Moments/Cultural_Health Moments_Data.csv')
    return df

#loading the list into a pandas dataframe
data = load_data()

data[['Important_Date_1','Important_Date_2']] = data[['Important_Date_1','Important_Date_2']].apply(pd.to_datetime)
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
st.markdown("Sirui Yang, Kuzi Rusere, Ye An & Umair Shaikh")



row0_space1, row0_1, row0_space2, row0_2, row0_space3 = st.columns((.1, 1, .1, 1, .1))

with row0_1:
    st.subheader("**Vision:**")
    st.markdown("Understanding how cultural health moments"
                "impact health consumers’ digital search behavior may provide insight into potential" 
                "interception points relating to disease-state awareness, education, symptoms, diagnosis, and/or treatment.")

with row0_2:
    st.subheader("**Issue:**")
    st.markdown("During high-profile health moments "
                "(ex. – the cancer-related deaths of Chadwick Boseman and Eddie Van Halen, "
                "or the cancer diagnosis of Jimmy Carter or Rush Limbaugh) digital health consumers’ "
                "initial search queries are typically surface-level search (ex. – scandal, wealth, career highlights, spouse, etc.), "
                "but that search behavior shifts to awareness, signs, symptoms, and introspection over time. Understanding that time "
                "horizon – when the shift occurs and what common topical trends exist – may provide opportunities to engage by leveraging "
                "naturally occurring awareness and search.")

st.markdown("---")

row1_space1, row1_1, row1_space2, row1_2, row1_space3 = st.columns((.1, 1, .1, 1, .1))

with row1_1:
    st.subheader("**Methodology:**")
    st.markdown("Examination of publicly available search data as related to high-profile disease state diagnosis and/or deaths. ")

with row1_2:
    st.markdown("For the data collection in this project we are going to use Google Trend specifically PyTrends. "
                "Google Trends is a website by Google that analyzes the popularity of top search queries in Google Search across various regions and languages. "
                "The website uses graphs to compare the search volume of different queries over time. "
                "PyTrends inturn is a Python library/module/API that Allows simple interface for automating downloading of reports from Google Trends")

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

        

with row2_2:
    if x == 0:
        num = dict_mapper.get(choice)
        name = data['Name_of_HPP'][num]
        condition = data['Chronic_Condition'][num]
        Date1 = str(data.Important_Date_1[num].date())
        Date2 = str(data.Important_Date_2[num].date())

        st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Name:</b> {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Chronic Condition:</b> {condition}</p>", unsafe_allow_html=True)
        
        if str(data.Important_Date_2[num]) != 'NaT':
            st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>First Important Date:</b> {Date1}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Second Important Date:</b> {Date2}</p>", unsafe_allow_html=True)

        else:
            st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Important Date:</b> {Date1}</p>", unsafe_allow_html=True)
            
    else:
        st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Name:</b> {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Chronic Condition:</b> {condition}</p>", unsafe_allow_html=True)
        try:
            if check:
                st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>First Important Date:</b> {Date1}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Second Important Date:</b> {Date2}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='text-align: center;'><b style= 'color:navy;'>Important Date:</b> {Date1}</p>", unsafe_allow_html=True)

        except:
            st.write("")
    Date = Date1
    if Date2 not in ['NaT', '']:
        chosen_date = st.radio( "Please choose one:", ('First Important Date', 'Second Important Date'))
        if chosen_date == 'First Important Date':
            Date = Date1
        else:
            Date = Date2
    else:
        st.write("")

@st.cache(allow_output_mutation=True)
def create_date_interval(date):
    """
    This fuction creates the date interval needed for as one of the parameters for the pytrend.build_payload fuction
    The function takes in the important date and returns a string of the date interval +/- 30 days
    """
    date = datetime.datetime.fromisoformat(date)
    start_date = date - datetime.timedelta(days= 30)
    end_date = date + datetime.timedelta(days=30)

    x = (str(start_date)).split()[0]
    y = (str(end_date)).split()[0]
    
    date_interval = f"{x} {y}"

    return date_interval


@st.cache(allow_output_mutation=True)
def get_trend_suggested_keyword(string_list):
    """  
    This fuction returns the google trends suggested keyword
    It inputs either the Name of the high profile person or the Chronic Condition
    It passes that to the pytrends fuction suggestions 
    """
    keyword = pytrend.suggestions(keyword=string_list)[0]['mid']
    return keyword


@st.cache(allow_output_mutation=True)
def dataframe_of_trends(HPP_name, Chronic_Condition, Date):
    """
    This fuction outputs a dataframe of the trends data/results from google trends
    It inputs the index from the 'data' dataframe which is housing the Cultural health moments High Profile people and chronic condition data 
    it will also output dictionary of the 'related, top and rising queries' which we will need for later.  
    """
    #setting up the parameters for the payload
    KEYWORDS=[get_trend_suggested_keyword(HPP_name), get_trend_suggested_keyword(Chronic_Condition)]
    DATE_INTERVAL= create_date_interval(Date)
    COUNTRY="US" 
    CATEGORY = 0 
    SEARCH_TYPE=''
    #######################
    #the below is building the payload using the above parameters
    pytrend.build_payload( kw_list= KEYWORDS, timeframe = DATE_INTERVAL, geo = COUNTRY, cat=CATEGORY,gprop=SEARCH_TYPE) 
    df = pytrend.interest_over_time() #we will  assign the interest_overtime/trends dataframe to df
    #now we will rename the column name from the pytrends suggested mid value to the actual name of the high profile person and chronic condition 
    df = df.rename(columns={KEYWORDS[0]: HPP_name, KEYWORDS[1]: Chronic_Condition})
    df.drop('isPartial', axis=1, inplace=True)
    df.reset_index(inplace=True)

    #now we will grab the dictionary of the related, top and rising queries and rename the keys
    related_queries = pytrend.related_queries()
    related_queries[HPP_name] = related_queries.pop(KEYWORDS[0])
    related_queries[Chronic_Condition] = related_queries.pop(KEYWORDS[1])
    #now we will seperate the dictionary into HPP_related_queries and the CC_related_queries 
    HPP_related_queries = related_queries[HPP_name]
    CC_related_queries = related_queries[Chronic_Condition]

    df_region = pytrend.interest_by_region()
    #now we will rename the column name from the pytrends suggested mid value to the actual name of the high profile person and chronic condition 
    df_region.reset_index(inplace=True)
    df_region = df_region.rename(columns={'geoName':'State',KEYWORDS[0]: HPP_name, KEYWORDS[1]: Chronic_Condition})
    

    return df, HPP_related_queries, CC_related_queries, DATE_INTERVAL, df_region

@st.cache(allow_output_mutation=True)   
def get_top_and_rising(related_queries_dict):
    """  
    This fuction returns the top and rising related queries 
    """
    # for rising related queries
    related_queries_rising = related_queries_dict.get('rising')
    # for top related queries
    related_queries_top = related_queries_dict.get('top')

    return related_queries_rising, related_queries_top

@st.cache(allow_output_mutation=True)
def Topbar_chart(df):
    fig = px.bar(df, 
                title= f"This is a bar chart of {a}",
                x=f'{df.columns[1]}', 
                y=f'{df.columns[0]}', 
                height=500, 
                width=800)
    return fig


@st.cache(allow_output_mutation=True)
def Risingbar_chart(df):
    fig = px.bar(df, 
                title= f"This is a bar chart of {b}",
                x=f'{df.columns[1]}', 
                y=f'{df.columns[0]}', 
                height=500, 
                width=800)
    return fig

@st.cache(allow_output_mutation=True)
def wordcloud_of_related_queries(df, title):
    tuples = [tuple(x) for x in df.values]
    wordcloud = WordCloud().generate_from_frequencies(dict(tuples))
    fig = plt.figure(figsize = (10, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title(title)
    
    return fig
############################################################


try:
    df, HPP_related_queries, CC_related_queries, date_interval, df_region = dataframe_of_trends(name, condition, Date)
    col4, col5, col6 = st.columns((.35,1,.1))
    with col4:
        st.write("")
    with col5:
        fig = px.line(df, x='date', y=df.columns[1:3],width=900, height=600)
        fig.update_layout(title=f"Trend Plot for {name} and {condition} within +/- 30 days of {Date}")
        st.plotly_chart(fig)
    with col6:
        st.write("")

    #############################################################################################

    st.markdown("---")

    a = f"Top Related Quires for {df.columns[1]}"
    b = f'Rising Related Quiries for {df.columns[1]}'

    related_queries_rising, related_queries_top = get_top_and_rising(HPP_related_queries)
    dfA = related_queries_top
    dfB = related_queries_rising

    row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns((.1, 1, .1, 1, .1))

    with row4_1:
        st.markdown(f'Top Related Quires for {df.columns[1]}')
        st.table(dfA.head())
        st.plotly_chart(Topbar_chart(dfA))
        fig = wordcloud_of_related_queries(dfA, f'Top Related Quires for {df.columns[1]}')
        st.pyplot(fig)

    with row4_2:
        st.markdown(f'Rising Related Quiries for {df.columns[1]}')
        st.table(dfB.head())
        st.plotly_chart(Risingbar_chart(dfB))
        fig = wordcloud_of_related_queries(dfB, f'Rising Related Quiries for {df.columns[1]}')
        st.pyplot(fig)



    st.markdown("---")
    a = f"Top Related Quires for {df.columns[2]}"
    b = f"Rising Related Quiries for {df.columns[2]}"

    related_queries_rising, related_queries_top = get_top_and_rising(CC_related_queries)
    dfA = related_queries_top
    dfB = related_queries_rising

    row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns((.1, 1, .1, 1, .1))

    with row5_1:
        st.markdown(f'Top Related Quires for {df.columns[2]}')
        st.table(dfA.head())
        st.plotly_chart(Topbar_chart(dfA))
        fig = wordcloud_of_related_queries(dfA, f'Top Related Quires for {df.columns[2]}')
        st.pyplot(fig)

    with row5_2:
        st.markdown(f'Rising Related Quiries for {df.columns[2]}')
        st.table(dfB.head())
        st.plotly_chart(Risingbar_chart(dfB))
        fig = wordcloud_of_related_queries(dfB, f'Rising Related Quiries for {df.columns[2]}')
        st.pyplot(fig)


    df_region['Code'] = df_region['State'].map(code)

    row6_space1, row6_1, row6_space2, row6_2, row6_space3 = st.columns((.1, 1, .1, 1, .1))

    with row6_1:
        fig = px.choropleth(df_region, title= f'Google Trends interest of {df_region.columns[1]} over the date interval {date_interval}',
                            locations='Code',
                            color=f'{df_region.columns[1]}',
                            color_continuous_scale='spectral_r',
                            hover_name='State',
                            locationmode='USA-states',
                            scope='usa', 
                            height=500, 
                            width=700)

        fig.add_scattergeo(
                    locations=df_region['Code'],    ###codes for states,
                    locationmode='USA-states',
                    text=df_region['Code'],
                    mode='text')

        st.plotly_chart(fig)

    with row6_2:
        fig = px.choropleth(df_region,
                            title= f'Google Trends interest of {df_region.columns[2]} over the date interval {date_interval}',
                            locations='Code',
                            color=f'{df_region.columns[2]}',
                            color_continuous_scale='spectral_r',
                            hover_name='State',
                            locationmode='USA-states',
                            scope='usa', 
                            height=500, 
                            width=700)

        fig.add_scattergeo(
                    locations=df_region['Code'],    ###codes for states,
                    locationmode='USA-states',
                    text=df_region['Code'],
                    mode='text')

        st.plotly_chart(fig)
except:
    st.write("THERE WAS AN EXCEPTION!!")