# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Machine Learning, NLP, and Streamlit**. The application extracts text from PDF resumes, predicts the resume's domain, analyzes technical skills based on a selected target role, calculates a resume score, identifies missing skills, and provides personalized improvement suggestions.

---

## 🚀 Features

- 📄 Upload resumes in PDF format
- 🤖 Predict resume domain using Machine Learning
- 🎯 Select a target job role for comparison
- ⭐ Calculate a resume score
- 🛠 Detect technical skills
- ❌ Identify missing skills
- 💡 Generate personalized resume improvement suggestions
- 🌐 Interactive Streamlit web interface

---

## 🖼 Project Demo

### Home Page

> *(Add a screenshot here after deployment)*

### Analysis Result

> *(Add a screenshot showing the resume score, detected skills, missing skills, and suggestions.)*

---

## 🏗 Project Architecture

```
                PDF Resume
                     │
                     ▼
             Text Extraction
               (pdfplumber)
                     │
                     ▼
          NLP Preprocessing
   (Tokenization, Stopword Removal,
        Lemmatization, Cleaning)
                     │
                     ▼
          TF-IDF Vectorization
                     │
                     ▼
     Logistic Regression Model
                     │
                     ▼
      Resume Category Prediction
                     │
                     ▼
      Skill Gap Analysis
                     │
                     ▼
 Resume Score & Suggestions
                     │
                     ▼
          Streamlit Dashboard
```

---

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer

### Natural Language Processing

- NLTK
- Tokenization
- Stopword Removal
- Lemmatization

### Frontend

- Streamlit

### PDF Processing

- pdfplumber

### Data Processing

- Pandas
- NumPy

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
AI-Resume-Analyzer
│
├── dataset/
│   ├── UpdatedResumeDataSet.csv
│
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── uploads/
│
├── app.py
├── predict.py
├── preprocess.py
├── skills.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Trait-Analyzer.git
```

Go to the project directory

```bash
cd AI-Resume-Trait-Analyzer
```

Create a virtual environment

### Windows

```bash
python -m venv venv
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

or

```bash
python3 -m streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 🧠 Machine Learning Workflow

1. Load resume dataset
2. Clean resume text using NLP
3. Convert text into TF-IDF vectors
4. Train a Logistic Regression classifier
5. Save trained model
6. Upload a new resume
7. Predict resume domain
8. Compare detected skills with the selected role
9. Calculate resume score
10. Generate improvement suggestions

---

## 📊 Current Features

- Resume domain prediction
- Resume score calculation
- Technical skill extraction
- Missing skill identification
- Resume improvement suggestions
- Confidence score display
- Role-based analysis

---

## 🔮 Future Improvements

- Resume keyword highlighting
- ATS compatibility score
- Interactive charts and analytics
- Resume summarization using LLMs
- Support for DOCX resumes
- Deploy on Streamlit Community Cloud

---

## 👩‍💻 Author

**Aditi Choudhury**

B.Tech CSE Student

Interested in:
- Artificial Intelligence
- Machine Learning
- Data Analytics
- Backend Development

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: *(Add your LinkedIn profile here)*

---


## 🌐 Live Demo

https://ai-resume-trait-analyzer.streamlit.app

## ⭐ If you found this project useful, consider giving it a star!