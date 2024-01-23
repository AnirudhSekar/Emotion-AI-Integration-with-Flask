import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
def analyze_sentiment(text):
    
    sid = SentimentIntensityAnalyzer()
    polarity_scores = sid.polarity_scores(text)
    
    if polarity_scores['pos'] >= polarity_scores['neg'] and polarity_scores['compound'] >=0.05:
        return ("Positive", polarity_scores['pos'], polarity_scores['neu'],polarity_scores['neg'], polarity_scores['compound'])
    else:
        return ("Negative", polarity_scores['pos'], polarity_scores['neu'],polarity_scores['neg'],polarity_scores['compound'])
    