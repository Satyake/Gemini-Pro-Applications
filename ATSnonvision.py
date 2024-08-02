
import streamlit as st
import google.generativeai as genai 
import os 
import PyPDF2 as pdf 
GEMINI_API_KEY='AIzaSyCG9qaINdEYyfukj04JBQwXeP_PH0wErur8d0'

from dotenv import load_dotenv
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page_num in range(len(reader.pages)):
        page=reader.pages[page_num]
        text+=str(page.extract_text())
    return text




input_prompt="""
your an experienced HR manager, your task is to Review the CV/Resume,
with tech experience. Please share professional evalulation
on whether the candidates profile aligns with the job description.
Highlight the candiates strengths and weakness in relation to the job.
Match based on jd and missing keywords.
resume:{text}
description:{jd}

I want the response i none single string having the form
{{"JD Match" : "%", "MissingKeywords:[]","Profile Summary":""}}
"""

st.title("Smart STS")
st.text("Improve your Resume ATS")
jd=st.text_area("Paste the JD here")
uploaded_file=st.file_uploader("Upload your Resume", type="pdf")
submit=st.button('Submit')

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)
        