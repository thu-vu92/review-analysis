import emoji

def clean_review_text(review):

    # Convert text to lowercase
    review = review.lower()

    # Replace emojis with text
    review_text = emoji.demojize(review)

    return review_text