import pickle
from preprocess import preprocess_text

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

# Load TF-IDF vectorizer
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))


def predict_category(resume_text):
    # Clean the resume
    cleaned_text = preprocess_text(resume_text)

    # Convert to TF-IDF vector
    vector = vectorizer.transform([cleaned_text])

    # Predict category
    prediction = model.predict(vector)

    return prediction[0]


# Test the model
sample_resume = """
Managed a team of 12 students during a hackathon.
"""
print("Predicted Category:", predict_category(sample_resume))