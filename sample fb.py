# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:57:24 2018

@author: Dimpy
"""
import requests 
import json 
import pandas as pd
import os, sys
import numpy as np
from textblob import TextBlob
import re

token = "EAACEdEose0cBAFPkGQ2kUimzygKS8vjWj2yWceZC1SbacptWZBUj3sRksQN51nl7gLf8aFZBgXiIsKXtqTGEp4QFJaPYdCoONEm6vk9Y8ekNVIgYLMjbhE7jIvHlYiZBkmumgwS3zoxiu1Vu8UGU7KfVVsCHKZAE5a7k7dccH365gm2Y733iZBJLzFkGbXybcbB3eoYCnB9AZDZD"

try:
    token = os.environ['FB_TOKEN']
except:
   print ("EAACEdEose0cBAFPkGQ2kUimzygKS8vjWj2yWceZC1SbacptWZBUj3sRksQN51nl7gLf8aFZBgXiIsKXtqTGEp4QFJaPYdCoONEm6vk9Y8ekNVIgYLMjbhE7jIvHlYiZBkmumgwS3zoxiu1Vu8UGU7KfVVsCHKZAE5a7k7dccH365gm2Y733iZBJLzFkGbXybcbB3eoYCnB9AZDZD")
   sys.exit(-1)

fb_pageid = "524628374230596"
fb_postid = "2323390214354394"
commentlst = []
datelst = []

url = "https://graph.facebook.com/v3.0/"+ fb_pageid +"_"+ fb_postid +"/comments?limit=100&access_token="+token

while(True):
    posts = requests.get(url)
    posts_json = posts.json()
    for x1 in posts_json['data']:
        commentlst.append(x1.get('message').encode('utf-8').strip())
        datelst.append(x1.get('created_time'))
    next_page = ""
    try:
        next_page = posts_json['paging']['next']
        url = next_page
    except:
        break
    if not next_page: break
    print ("Count: %s,  Next Page: %s" % ( len(commentlst), url))

print ("\nGenerating JSON File")

df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
df['dates'] = pd.to_datetime(df['dates'])
df['day_of_week'] = df['dates'].dt.weekday_name
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['count'] = 1 

#df.to_json('comment_data.json')

df_message=df[['comment']]

a=df_message.iloc[0]
b=str(a)
def clean_tweet(message):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",str( message).split()))
def analize_sentiment(message):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(message))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

analize_sentiment(b)

"""from google.cloud import language, exceptions

client = language.Client()
# export GOOGLE_APPLICATION_CREDENTIALS environment variable 

with open('comment_data.json') as data_file:
    data = json.load(data_file)

sentiment_list = []
for x1,y1  in data['comment'].items():
   # try:
        document = client.document_from_text(y1)
        sentiment = document.analyze_sentiment().sentiment
        sentiment_list.append({"id": x1, "comment": y1, "sentiment_score": sentiment.score, "sentiment_magnitude": sentiment.magnitude })
        print ("Pass")
    except:
        print ("Fail")

with open('sentiment_comments.json', 'w') as outfile:
    json.dump(sentiment_list, outfile)"""