import pickle
from preprocess import preprocess_text

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

# Load TF-IDF vectorizer
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))


def predict_category(resume_text):

    cleaned_text = preprocess_text(resume_text)

    vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)