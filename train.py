import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from preprocess import preprocess_text
df = pd.read_csv("dataset/Resume.csv")
print(df.head())
df["Cleaned_Resume"] = df["Resume"].apply(preprocess_text)
print(df[["Resume", "Cleaned_Resume"]].head())

print("Step 1: Creating TF-IDF")
vectorizer = TfidfVectorizer(max_features=5000)

print("Step 2: Transforming text")
X = vectorizer.fit_transform(df["Cleaned_Resume"])

print("Step 3: Labels")
y = df["Category"]

print("Step 4: Splitting dataset")
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Step 5: Training model")
model = LogisticRegression()

model.fit(X_train, y_train)

print("Step 6: Predicting")
y_pred = model.predict(X_test)

print("Step 7: Accuracy")
print("Accuracy:", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

print("Step 8: Saving model")
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model saved successfully!")