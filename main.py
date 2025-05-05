import os
from key import groq_key  # Make sure key.py contains: groq_key = "your-api-key"

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import streamlit as st

# Set Groq API Key and endpoint
os.environ["OPENAI_API_KEY"] = groq_key  # Required by LangChain
openai_api_base = "https://api.groq.com/openai/v1"

# Initialize LLM with Groq's endpoint
llm = ChatOpenAI(
    openai_api_key=groq_key,
    openai_api_base=openai_api_base,
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # Or another supported model: llama3-8b-8192, etc.
    temperature=0.8
)

# Streamlit UI
st.title("LLM with LangChain _tgpt (Groq API)")
input_text = st.text_area("enter your text here")

if input_text:
    response = llm([HumanMessage(content=input_text)])
    st.write("Response:", response.content)
