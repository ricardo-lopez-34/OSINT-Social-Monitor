# OSINT Social Monitor 🛰️

An Open Source Intelligence tool that monitors social media keywords for emergency management and threat detection using real-time sentiment analysis.

## Description
An Open Source Intelligence tool designed for real-time monitoring of social media keywords to detect emerging security threats and support emergency management through sentiment analysis and geographic data.

## Key Features
- **Keyword Tracking:** Monitors specific phrases related to public safety or infrastructure threats.
- **Sentiment Analytics:** Classifies public mood into positive, neutral, or "Alert" categories.
- **Crisis Mapping:** Visualizes the geographic density of social mentions during an incident.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, TextBlob, Tweepy, Plotly
- **Model:** Natural Language Processing (NLP) for sentiment classification.

## Engineering Logic
- **Backend:** The monitor uses asynchronous requests to pull data streams and applies a scoring algorithm to distinguish between casual mentions and emergency signals.
- **Software Engine:** A Streamlit dashboard displays a "Threat Pulse" meter and a live ticker of relevant public data points.
