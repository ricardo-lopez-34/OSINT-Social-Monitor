import streamlit as st
import pandas as pd
import numpy as np
from textblob import TextBlob
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import random

st.set_page_config(page_title="OSINT Sentinel", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #58a6ff; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

if 'osint_feed' not in st.session_state:
    st.session_state.osint_feed = pd.DataFrame(columns=['Time', 'Source', 'Message', 'Sentiment', 'Risk'])

st.title("🛰️ OSINT Sentinel | Public Intelligence Monitor")
st.write("Real-time Social Stream Analysis for Emergency Response")

st.sidebar.title("📡 Tracking Parameters")
tracked_keywords = st.sidebar.multiselect("Active Keywords", 
    ["Wildfire", "Flood", "Cyber-Attack", "Protest", "Power Outage"],
    default=["Power Outage", "Cyber-Attack"])

placeholder = st.empty()

for i in range(100):
    msgs = [
        "Major blackout in sector 4, no power for 3 hours.",
        "System breach detected in local bank servers!",
        "Traffic is moving slow but everything looks safe.",
        "Heavy smoke seen near the industrial district.",
        "Routine server maintenance scheduled for tonight."
    ]
    
    selected_msg = random.choice(msgs)
    blob = TextBlob(selected_msg)
    sentiment = "Alert" if blob.sentiment.polarity < 0 else "Neutral"
    risk_val = random.randint(70, 95) if sentiment == "Alert" else random.randint(5, 30)
    
    new_data = {
        'Time': datetime.now().strftime("%H:%M:%S"),
        'Source': "@user_" + str(random.randint(100, 999)),
        'Message': selected_msg,
        'Sentiment': sentiment,
        'Risk': risk_val
    }
    
    st.session_state.osint_feed = pd.concat([pd.DataFrame([new_data]), st.session_state.osint_feed]).head(50)
    
    with placeholder.container():
        m1, m2, m3 = st.columns(3)
        avg_risk = st.session_state.osint_feed['Risk'].mean()
        m1.metric("Threat Pulse", f"{round(avg_risk, 1)}%", delta="-2.1%" if avg_risk < 50 else "+4.5%")
        m2.metric("Active Streams", len(tracked_keywords))
        m3.metric("System Status", "Scanning...")

        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.subheader("Live Intelligence Feed")
            st.dataframe(st.session_state.osint_feed, use_container_width=True)
            
        with col_right:
            st.subheader("Sentiment Distribution")
            if not st.session_state.osint_feed.empty:
                fig = px.bar(st.session_state.osint_feed, x='Sentiment', y='Risk', color='Sentiment',
                             color_discrete_map={'Alert':'#f85149', 'Neutral':'#30363d'})
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#58a6ff")
                st.plotly_chart(fig, use_container_width=True)

    time.sleep(2)
