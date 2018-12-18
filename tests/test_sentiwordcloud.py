#from .context
from app.sentiwordcloud import sentiWordCloud
import pytest

def test_get_tweets_returns_array():
    """
    GIVEN that we have a connection to twitter
    WHEN a new search word is provided
    THEN fetch a list of 10 tweets with that word
    """
    query = 'winnfield'
    tweetList = api.get_tweets(query)
    assert isinstance(tweetList , list)
    assert len(tweetList) == 10

def test_get_tweets_elements_have_text():
    """
    GIVEN that we have a connection to twitter
    WHEN a new search word is provided
    THEN check that the resultlist contains strings
    """
    query = 'winnfield'
    tweetList = api.get_tweets(query)
    assert isinstance(tweetList[0]['text'], str)

def test_get_clean_tweet():
    """
    GIVEN that we have a tweet with special characters
    WHEN a call is made to get a clean version of the tweet
    THEN a clean string is returned without special characters
    """
    query = "&winnfield"
    cleantweet = api.clean_tweet(query)
    assert cleantweet == "winnfield"

def test_get_tweet_sentiment_positive():
    """
    GIVEN that we have a tweet
    WHEN a call is made to get a sentiment
    THEN we get the positive sentiment back
    """
    query = "wonderful good great sunshine"
    result = api.get_tweet_sentiment(query)
    assert result == "positive"

def test_get_tweet_sentiment_negative():
    """
    GIVEN that we have a tweet
    WHEN a call is made to get a sentiment
    THEN we get the negative sentiment back
    """
    query = "bad awful horrid"
    result = api.get_tweet_sentiment(query)
    assert result == "negative"
