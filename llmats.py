#field to put the JD
#Upload PDF
#PDF to Image --> Processing--> Gemini
#PromptsTemplate[Multiple Prompts]

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai 
import base64
from IPython.display import Image
from IPython.core.display import HTML

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    ##convert the PDF to image
    if uploaded_file is not None:
    #convert to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]
        #convert to bytes 
        img_byte_arr=io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr=img_byte_arr.getvalue()
        pdf_parts=[
            {
                "mime_type":"image/jpeg",
                "data":base64.b64encode(img_byte_arr).decode('utf-8')
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")


#create streamlit application 

st.set_page_config(page_title='ATS Resume Expert')
st.header("ATS Tracking System")
input_text=st.text_area("Enter the Job Description", key="input")

#create uploaded file 
uploaded_file=st.file_uploader("Upload your CV/Resume(PDF)", type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded!")

submit1=st.button("Tell me about the Resume/CV")

submit2=st.button("Percentage match")

#submit3=st.button("Percentage match")


input_prompt1="""
your an experienced HR manager, your task is to Review the CV/Resume,
with tech experience. Please share professional evalulation
on whether the candidates profile aligns with the job description.
Highlight the candiates strengths and weakness in relation to the job.
"""

input_prompt2="""
Your a skilled ATS Scanner, with a deep understanding of 
data science , analyst, AI , Big data functionality. 
your task is evaluate the resume and give percentage match 
based on the keywords used in the Resume/CV
"""
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please upload the Resume/CV(PDF)")
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is :")
        st.write(response)
    else:
        st.write("Please upload the Resume/CV(PDF)")
    
