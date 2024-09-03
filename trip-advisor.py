import streamlit as st

# Import the recommendation function
from recommendation_logic import recommend_similar_reviews

# Title of the app
st.title('Hotel Review Recommendation System')

# Input text for the review
input_review = st.text_area('Enter a hotel review to find similar reviews:', height=200)

# Number of recommendations
top_n = st.slider('Number of recommendations:', min_value=1, max_value=10, value=5)

# Button to generate recommendations
if st.button('Get Recommendations'):
    if input_review:
        recommendations = recommend_similar_reviews(input_review, top_n)
        
        # Display the recommendations
        st.write(f"**Top {top_n} Similar Reviews:**")
        for i, row in recommendations.iterrows():
            st.write(f"**Rating:** {row['Rating']}")
            st.write(f"**Review:** {row['Review']}")
            st.write('---')
    else:
        st.warning('Please enter a review to get recommendations.')
