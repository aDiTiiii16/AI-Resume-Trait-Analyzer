import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from preprocess import preprocess_text

# Load dataset
df = pd.read_csv("dataset/Resume.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# Keep only required columns
df = df[["Resume_str", "Category"]]

# Remove empty rows
df.dropna(inplace=True)

# Preprocess resumes
df["Cleaned_Resume"] = df["Resume_str"].apply(preprocess_text)

print("\nSample Cleaned Data")
print(df[["Resume_str", "Cleaned_Resume"]].head())

# Convert text to numerical features
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["Cleaned_Resume"])

y = df["Category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("\nModel Saved Successfully!")