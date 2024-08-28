"""This file contains the functions required for the NLP task

    The task involves obtaining the sentiments of a corpus of Amazon reviews.
    This is done using SpaCy and Textblob. 

    Running this file may take many minutes or even longer. The output will be
    five randomly selected positive and five randomly selected negative 
    reviews and their assessed similarites along with the intermediate cleaned
    version of the review. 

    The entire output dataset can be obtained by uncommenting the .to_csv line.
"""
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Choose the language model and sentiment analysis methods
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Load the dataset, uncomment and change example location as appropriate
#df = pd.read_csv('D:/Documents/CoGrammar/Task Repo/CoGrammar/Tasks/Task 26/1429_1.csv')

# Select only the reviews column
reviews_data = pd.DataFrame(df['reviews.text'])

# Remove any rows where the review text is missing
reviews_data.dropna(inplace=True)


# Clean and the text in the reviews and remove stop words
def tokenise(review):
  review = str(review).lower().strip()

  doc = nlp(review)
  tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
  return ' '.join(tokens)


reviews_data['reviews.tokens'] = reviews_data['reviews.text'].apply(tokenise)


# Analyse the sentiment using polarity
def analyse_sentiment(review):
    doc = nlp(review)

    polarity = doc._.blob.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


reviews_data['reviews.sentiment'] = reviews_data['reviews.tokens'].apply(analyse_sentiment)

# Look at five positive and five negative reviews
positive_reviews = reviews_data[reviews_data['reviews.sentiment'] == "Positive"]
negative_reviews = reviews_data[reviews_data['reviews.sentiment'] == "Negative"]
neutral_reviews = reviews_data[reviews_data['reviews.sentiment'] == "Neutral"]

sample_reviews = positive_reviews.iloc[0:5]
sample_reviews = pd.concat([sample_reviews, negative_reviews.iloc[0:5]])
sample_reviews = pd.concat([sample_reviews, neutral_reviews.iloc[0:5]])
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
print(sample_reviews)

# Uncomment this to save thw whole dataframe of sentiment to a csv
# reviews_data.to_csv('review_sentiments.csv')
