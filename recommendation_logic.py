from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your data
df = pd.read_csv('tripadvisor_hotel_reviews.csv')

# Preprocess the text data
df['cleaned_review'] = df['Review'].str.lower()

# Vectorize the review texts
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['cleaned_review'])

# Add sentiment analysis to the recommendations
df['sentiment'] = df['cleaned_review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Define a function to recommend similar reviews
def recommend_similar_reviews(input_text, top_n=5, sentiment_choice='All'):
    input_vector = tfidf_vectorizer.transform([input_text.lower()])
    similarity_scores = cosine_similarity(input_vector, tfidf_matrix).flatten()
    similar_indices = similarity_scores.argsort()[-top_n:][::-1]
    
    recommendations = df.iloc[similar_indices][['Review', 'Rating', 'sentiment']]
    
    if sentiment_choice == 'Positive':
        recommendations = recommendations[recommendations['sentiment'] > 0]
    elif sentiment_choice == 'Negative':
        recommendations = recommendations[recommendations['sentiment'] < 0]
    
    return recommendations
