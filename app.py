import streamlit as st
import pdfplumber

from predict import predict_category
from skills import (
    extract_skills,
    calculate_score,
    get_missing_skills,
    generate_suggestions
)


def extract_text(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and compare it with the selected job role.")

role = st.selectbox(
    "🎯 Select Target Role",
    [
        "Software Developer",
        "Full Stack Developer",
        "Data Analyst",
        "Machine Learning Engineer"
    ]
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Analyze Resume"):

        resume_text = extract_text(uploaded_file)

        prediction = predict_category(resume_text)

        skills = extract_skills(resume_text, role)

        score = calculate_score(skills, role)

        missing = get_missing_skills(skills, role)

        suggestions = generate_suggestions(score, missing)

        st.success(f"### ✅ Resume Category: {prediction}")

        st.metric("⭐ Resume Score", f"{score}/100")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🛠 Detected Skills")

            if skills:
                for skill in skills:
                    st.success(skill.title())
            else:
                st.warning("No matching skills detected.")

        with col2:

            st.subheader("📌 Missing Skills")

            if missing:
                for skill in missing:
                    st.error(skill.title())
            else:
                st.success("No important skills missing.")

        st.divider()

        st.subheader("💡 Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.write(f"✔ {suggestion}")
        else:
            st.success("Excellent Resume!")