import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

def preprocess_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words and lemmatize
    cleaned_words = []

    for word in words:
        if word not in stop_words:
            cleaned_word = lemmatizer.lemmatize(word)
            cleaned_words.append(cleaned_word)

    # Join words back into a sentence
    return " ".join(cleaned_words)