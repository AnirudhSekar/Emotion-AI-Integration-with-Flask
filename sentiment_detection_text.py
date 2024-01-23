import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
def analyze_sentiment(text):
    
    sid = SentimentIntensityAnalyzer()
    polarity_scores = sid.polarity_scores(text)
    
    if polarity_scores['compound'] >= 0.05:
        return ("Positive", polarity_scores['pos'], polarity_scores['neu'],polarity_scores['neg'], polarity_scores['compound'])
    elif polarity_scores['compound'] <= -0.05:
        return ("Negative", polarity_scores['pos'], polarity_scores['neu'],polarity_scores['neg'],polarity_scores['compound'])
    elif polarity_scores['compound'] >= -0.05 and polarity_scores['compound'] <=0.05 or (polarity_scores['pos']-polarity_scores['neg'])*100 <= 5:
        return ("Neutral", polarity_scores['pos'], polarity_scores['neu'],polarity_scores['neg'],polarity_scores['compound'])
    
