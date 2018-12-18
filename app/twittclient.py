#! /usr/bin/env python
import re
import tweepy
import os
from tweepy import OAuthHandler
from textblob import TextBlob
from app import sentiwordcloud

class TwitterClient(object):
    def __init__(self):
        consumer_key = os.environ.get('API_KEY')
        consumer_secret = os.environ.get('API_SECRET_KEY')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(tweet)
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
            '''
            Main function to fetch tweets and parse them.
            '''
            # empty list to store parsed tweets
            tweets = []
            # print("Get_tweets called :",self,query,count)
            try:
                # print ("getting tweets")
                # call twitter api to fetch tweets
                fetched_tweets = self.api.search(q = query, count = count)
                # parsing tweets one by one
                # print ("got the tweets")
                #print (fetched_tweets)

                cleanStrArray = []
                cleanstr = ""
                for tweet in fetched_tweets:
                    # empty dictionary to store required params of a tweet
                    parsed_tweet = {}

                    # saving text of tweet
                    parsed_tweet['text'] = tweet.text

                    cleanstr = self.clean_tweet(tweet.text)
                    cleanStrArray.append(cleanstr)
                    # saving sentiment of tweet
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(cleanstr)

                    # appending parsed tweet to tweets list
                    if tweet.retweet_count > 0:
                        # if tweet has retweets, ensure that it is appended only once
                        if parsed_tweet not in tweets:
                            tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)

                # return parsed tweets
                sentiwordcloud.sentiWordCloud(cleanStrArray,query)
                return tweets

            except tweepy.TweepError as e:
                # print error (if any)
                print("Error : " + str(e))
