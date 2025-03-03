# getting required libraries
import streamlit as st
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer

# initialize vader sentiment analyzer
analyzer=SentimentIntensityAnalyzer()
st.title("Sentiment Analysis")
st.write("Enter the text below to analyze its sentiment....")
user_input=st.text_area("Enter the text","")
sentiment_scores=analyzer.polarity_scores(user_input)
sentiment_score=sentiment_scores["compound"]

# determine the sentiment
if sentiment_score>=0.05:
    sentiment="Positive 😊 "
elif sentiment_score<=-0.05:
    sentiment="Negative 😢"
else:
    sentiment="Neutral 👍"

#Display results
st.button("Sentiment")
st.subheader("Sentiment Analysis Results")
st.write(f"** sentiment **: {sentiment}")
st.write(f"*polarity_score*: {sentiment_score:.2f}")
