# Sentiment Analysis for Aviation Industry Tweets 
![](images/introduction.jpg)

---
<img src="images/matplotlib-logo.png" alt="Matplotlib Logo" width="130"/> <img src="images/numpy-logo.png" alt="Numpy Logo" width="130"/> <img src="images/pandas-logo.jpg" alt="Pandas Logo" width="130"/> <img src="images/streamlit-logo.jpg" alt="Streamlit Logo" width="130"/> <img src="images/plotly-logo.png" alt="Plotly Logo" width="130"/>

## Introduction
This project focuses on analyzing tweets related to the aviation industry using sentiment analysis techniques. This dashboard was developed for more practice, the main objective is explore how passengers perceive airlines based on their Twitter activity. By building an interactive data dashboard with Streamlit in Python, this simple project enables users to visualize, explore, and interact with tweet sentiment data efficiently.


## Problem Statement
Companies often face challenges in managing public sentiment, especially on social media platforms. This project tries to analyze the sentiments expressed in tweets about different airlines in U.S., providing insights into positive, neutral, and negative feedback. The key objectives include identifying trends in passenger opinions, visualizing sentiment distribution by airline, and pinpointing areas of improvement based on tweets content.

## Skills/Concepts demostrated
- Data loading and processing
- Streamlit application development
- Data visualization
- Natural language processing (NLP)

## Features
An examples of some features detailed below is the next screenshot of the main dashboard screen.

<img src="images/dashboard.png" alt="Dashboard" width="750"/>

1. **Random Tweet Display:**
   - Users can select a sentiment (positive, neutral, or negative) from the sidebar to view a random tweet matching the selected category.
     
2. **Sentiment Distribution Visualization:**
   - Displayed the number of tweets by sentiment using histograms and pie charts, with options to interchange between visualization types.
     
3. **Temporal and Geographic Analysis:**
   - Filtered tweets by the hour of the day to show user activity patterns.
   - Mapped tweet locations to identify geographical trends based on the time of day.
     
4. **Airline Sentiment Breakdown:**
   - Enabled users to select specific airlines and view sentiment distributions through interactive histograms.
     
5. **Word Cloud Generation:**
   - Created word clouds for positive, neutral, and negative sentiments, highlighting the most frequently used words.
     An example of the Word Cloud is the next image, showing negative sentiment for Southwest Airline.

     <img src="images/negative-sentiment-example.png" alt="Negative Sentiment Example" width="630"/>


## Finding and Insights
- **Sentiment Trends Across Airlines:** Airlines such as US Airways and American Airlines face the highest levels of negative feedback, pointing to delays, service quality, or comfort as major pain points. On the other hand, Virgin America, with only 35.91%, highlights operational efficiency and positive service experiences.
  
- **Activity Patterns:** Tweet activity peaks during common travel hours, such as between 7am to 10am, indicating critical times for managing customer interactions.
  
- **Frequent Themes in Feedback:** Words like "hour," "delay," and "service" highlight frustration due to delays and inconsistent service quality. On the other hand, words such as "Plane," "time," "air hostess," and "service" suggest that efficient service and flight quality keeps customers very satisfied.
  
- **Geographical Trends:** Sentiment clusters near major airport hubs highlight the impact of operational efficiency and issues with specific locations.







