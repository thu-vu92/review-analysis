import emoji

def clean_review_text(review):

    # Convert text to lowercase
    review = review.lower()

    # Replace emojis with text using emoji module
    reviews = emoji.demojize(review)

    return reviews