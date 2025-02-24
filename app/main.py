import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 CoolConnect - Cold Email Generator Tool 📧")
    url_input = st.text_input("Enter a URL:", value="", placeholder="🔗 URL Here...")
    submit_button = st.button("Create mail 🚀")

    