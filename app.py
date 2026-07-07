#Import Libraries
import streamlit as st
import pdfplumber

from predict import predict_category

#Extract Text from PDF
def extract_text(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text

#Create the UI
st.title("AI Resume Trait Analyzer")

st.write("Upload your resume in PDF format.")

#Upload Button
uploaded_file = st.file_uploader(
    "Choose a Resume",
    type=["pdf"]
)

#Analyze Button
if uploaded_file is not None:

    if st.button("Analyze Resume"):

        resume_text = extract_text(uploaded_file)

        prediction = predict_category(resume_text)

        st.success(f"Predicted Category: {prediction}")