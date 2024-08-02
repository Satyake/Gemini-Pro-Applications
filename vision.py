from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import vertexai
import google.generativeai as genai 
from vertexai.preview.generative_models import GenerativeModel
from PIL import Image

PROJECT_ID='mythical-style-346821'
LOCATION='us-central1'
GEMINI_API_KEY='AIzaSyCG9qaINdEYyfukj04JBQwXeP_PH0wEp_y'
os.environ['GCP_PROJECT_ID']=PROJECT_ID
os.environ['LOCATION']=LOCATION
os.environ['GEMINI_API_KEY']=GEMINI_API_KEY
vertexai.init(project="mythical-style-346821", location="us-central1")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-pro-vision")
#model=GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input!="":
        response=model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    return response.text

#initialize streamlit 
st.set_page_config(page_title="Gemini Image ")
st.header("Gemini Application")
input=st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image" , type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
                     image=Image.open(uploaded_file)
                     st.image(image, caption="Uploaded Image", use_column_width=True)
                     
            
submit= st.button("Tell me about the Image")

#if submit is clicked
if submit:
        response=get_gemini_response(input, image)
        st.subheader("the response is ")
        st.write(response)
