import re

def clean_review_text(review):

    # Convert text to lowercase
    review = review.lower()

    # Remove digits from text
    review = re.sub(r'\d+', '', review)

    return review