# Import Libraries
import streamlit as st
import pdfplumber

from predict import predict_category
from skills import extract_skills, calculate_score


# Extract Text from PDF
def extract_text(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Resume Trait Analyzer",
    page_icon="📄",
    layout="centered"
)

# Title
st.title("📄 AI Resume Trait Analyzer")
st.write("Upload your resume in PDF format and let AI analyze it.")


# Upload Button
uploaded_file = st.file_uploader(
    "Choose a Resume",
    type=["pdf"]
)


# Analyze Button
if uploaded_file is not None:

    if st.button("Analyze Resume"):

        # Extract resume text
        resume_text = extract_text(uploaded_file)

        # Predict category
        prediction = predict_category(resume_text)

        # Extract skills
        skills = extract_skills(resume_text)

        # Calculate score
        score = calculate_score(skills)

        # Display prediction
        st.success(f"Predicted Category: **{prediction}**")

        # Display score
        st.metric("Resume Score", f"{score}/100")

        # Display detected skills
        st.subheader("🛠 Detected Skills")

        if skills:
            for skill in skills:
                st.write(f"✅ {skill.title()}")
        else:
            st.warning("No skills detected.")