import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Setting up the main application title and sidebar title
st.title("Sentimental Analysis of Tweets about US Airlines")
st.sidebar.title("Sentimental Analysis of Tweets about US Airlines")

# Short description of the application
st.markdown("This application is a Streamlit dashboard to analyze the sentimental of Tweets")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentimental of Tweets")

# Path to the dataset
DATA_URL = r"C:\Users\danie\Desktop\Mauricie\Data Analyst\Projects\sentiment-analysis-for-aviation-industry-tweets\tweets.csv"

# Function to load data and cache it for faster subsequent access
@st.cache_data(persist=True)
def load_data():
    # Reading the dataset
    data = pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created']) # Converting the 'tweet_created' column to datetime for easier analysis
    return data

data = load_data() # Loading the data

# Sidebar widget to show a random tweet by sentiment type
st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative')) # Functionality for display random Tweets
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[["text"]].sample(n=1).iat[0,0]) # This is the column with the type of tweet
# The main idea here is to query the data for rows matching the selected sentiment and displays one random tweet's text

# Section to show the number of tweets by sentiment with visualization options
st.sidebar.markdown("### Number of tweets by sentiment")
select = st.sidebar.selectbox('Visualization type', ['Histogram', 'Pie chart'], key='1')
sentiment_count = data['airline_sentiment'].value_counts()
# Creating a DataFrame for sentiment counts
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values})

# Lets code a check box for show the graph.
if not st.sidebar.checkbox("Hide", True):
    st.markdown("### Number of tweets by sentiment")
    # Display a bar chart or pie chart based on user selection
    if select == "Histogram":
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

# Section for tweets by location and hour.
st.sidebar.subheader("When and where are users tweeting from?")
hour = st.sidebar.slider("Hour of day", 0, 23) # Slider to select hour
modified_data = data[data['tweet_created'].dt.hour == hour] # Filter tweets by selected hour

if not st.sidebar.checkbox("Close", True, key = 'close_checkbox_1'):
    st.markdown("### Tweets locations based on the time of day")
    # Display the number of tweets during the selected hour
    st.markdown("%i tweets between %i:00 and %i:00" % (len(modified_data), hour, (hour+1)%24)) #modified_data have the total of tweets
    st.map(modified_data) # Display tweets' geographic data on a map
    if st.sidebar.checkbox("Show raw data", False):
        st.write(modified_data) # Optionally display raw data

# Section to break down tweets by sentiment for specific airlines
st.sidebar.subheader("Breakdown airline tweets by sentiment")
choice = st.sidebar.multiselect('Pick airlines', ('American', 'Delta', 'Southwest', 'US Airways', 'United', 'Virgin America'), key='0')

# Implementation of the Functionality
if len(choice) > 0:
    choice_data = data[data.airline.isin(choice)]
    fig_choice = px.histogram(choice_data, x='airline', y='airline_sentiment', histfunc='count', color='airline_sentiment',
    facet_col='airline_sentiment', labels={'airline_sentiment':'tweets'}, height=600, width=800)
    st.plotly_chart(fig_choice)

# Word cloud section for visualizing frequently used words in tweets by sentiment
st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio('Display word cloud for what sentiment?', ('positive', 'neutral', 'negative'))

if not st.sidebar.checkbox("Close", True, key='3'):
    st.header('Word cloud for %s sentiment' % (word_sentiment))
    df = data[data['airline_sentiment']== word_sentiment] # Filter tweets by sentiment
    words = ' '.join(df['text']) # Combine all tweets into one string
    # Preprocess text: remove URLs, mentions, and retweet indicators
    procesed_words = ' '.join([word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT']) # Clearing of selected words
    # Generate word cloud
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', height=640, width=800).generate(procesed_words) # For display the words

    # Define the figure explicitly
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')  # Remove axis ticks and labels
    # PLT.IMSHOW(WORDCLOUD) # MATPLOTLB FOR THE DISPLAY
    # PLT.XTICKS([])
    # PLT.YTICKS([])
    st.pyplot(fig) # Streamlit for graphing the data
