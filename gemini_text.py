from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import vertexai
import google.generativeai as genai 
from vertexai.preview.generative_models import GenerativeModel
PROJECT_ID='mythical-style-346821'
LOCATION='us-central1'
import os
GEMINI_API_KEY='AIzaSyCG9qaINdEYyfukj04JBQwXeP_PH0wEo99s7sw'
os.environ['GCP_PROJECT_ID']=PROJECT_ID
os.environ['LOCATION']=LOCATION
os.environ['GEMINI_API_KEY']=GEMINI_API_KEY
vertexai.init(project="mythical-style-346821", location="us-central1")

#model=GenerativeModel("gemini-1.0-pro")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#function to load gemini pro model and get responses
model=genai.GenerativeModel('gemini-1.0-pro')
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#set up streamlit app 

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

## when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)