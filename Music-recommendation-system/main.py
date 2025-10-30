# Import necessary libraries
import pandas as pd
import numpy as np
import nltk
import pickle
import re

# 🧩 Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Load the CSV file
df = pd.read_csv('songdata.csv')

# Display first few rows
print(df.head(3))

# Randomly sample 5000 songs, drop the 'link' column, and reset index
df = df.sample(n=5000).drop('link', axis=1).reset_index(drop=True)

# Clean the 'text' column
df['text'] = (
    df['text']
    .str.lower()
    .replace(r'[^\w\s]', '', regex=True)
    .replace(r'\n', ' ', regex=True)
)

# Check cleaned text
print(df['text'][0])

# Stemming
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# Define a tokenization + stemming function
def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stems = [stemmer.stem(word) for word in tokens]
    return " ".join(stems)

# Apply tokenization
df['text'] = df['text'].apply(tokenization)

# TF-IDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(analyzer='word', stop_words='english')
matrix = tfidvector.fit_transform(df['text'])

# Compute cosine similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommendation(song_name):
    if song_name not in df['song'].values:
        return f"⚠️ Song '{song_name}' not found in dataset."

    idx = df[df['song'] == song_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    songs = [df.iloc[m_id[0]].song for m_id in distances[1:21]]
    return songs

# Test
print(recommendation('Alma Mater'))

# Save results
pickle.dump(similarity, open('similarity.pkl', 'wb'))
pickle.dump(df, open('df.pkl', 'wb'))
