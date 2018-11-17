
# coding: utf-8

# # Some ex to lear TextBlob

# In[2]:


from textblob import TextBlob


# In[3]:


wiki = TextBlob("Siraj is angry that he never gets good matches on TInder")


# In[4]:


wiki.tags


# In[5]:


wiki.words


# In[6]:


wiki.sentiment.polarity
#Thevalue is between -1 and +1


# # Sentiment analysis

# In[7]:


import tweepy


# In[8]:


# Step 1 - authenticate 
consumer_key = 'B3ptIr8Rv5RWv1xj8Xz16tu94'
consumer_secret = 'uhcUutjdwaC9jKBn47kJnXtHHLZ8OIm8VNpueucvjnGbnrqV55' 

access_token = '1063178501057056768-914TedwtxZAZfPMithKgEhtisYmNLV'
access_token_secret = 'YTBfUt0XE3ulWbf8cT7EsCcmllp8f2Mv9FqQ8Q6TQ9HQr' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[21]:


##Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


def get_label(analysis, threshold = 0):
    if analysis.sentiment[0] > threshold:
        return 'Positive'
    else:
        return 'Negative'

with open('tweets3.cv', 'w') as file:
    file.write('tweet,sentiment_label\n')
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        #Get the label corresponding to the sentiment analysis
        file.write('%s, %s \n \n' % (tweet.text.encode('utf8'), get_label(analysis)))
    

