import streamlit as st
import requests

# Set the page configuration
st.set_page_config(layout='wide')

# Fetch data from the API
topic = "cryptocurrency"
API_KEY = "962db8ac56fd4382b50a904a263aa1f2"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-05-25&sortBy=publishedAt&apiKey=962db8ac56fd4382b50a904a263aa1f2&language=en"

response = requests.get(url)
content = response.json()

# Display up to 5 articles
for i, article in enumerate(content["articles"][:5]):
    st.subheader(article["title"])
    st.write(article["description"])
    st.markdown(f"[Read More]({article['url']})", unsafe_allow_html=True)