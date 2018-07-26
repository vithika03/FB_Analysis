import requests 
import time
import pickle
import random
import numpy as np
import pandas as pd
token = "EAACEdEose0cBADwJ5oyRqoCbAVuLiqLdvQWdrdUWjnljSnfZChw3qfPkoTFuTvZCvFzUGSp5NGZA3GL97RxnJOrLtoxesMLZBkjiBLWmybIND0DZAUL1B1UlfTgjExox4MQDYFGbDLrHRR8kTun6rM9k7ZCKg3s6OGkKOFnHqZAAkoSYMOBBiRPwrvFZCVO4pTCaZAdiLrlSgewZDZD"

def req_facebook(req):
    
    r = requests.get("https://graph.facebook.com/v3.0/" + req , {'access_token' : token})
    
    return r
r=req_facebook("1500731676884280/posts?limit=4")
result=r.json()
data=[]
i=0
while True:
    try:
        time.sleep(random.randint(2,5))
        data.extend(result['data'])
        r=requests.get(result['paging']['next'])
        result= r.json()    
        i += 1
   
        if i > 5:
         break

    except:
        print ("done")
        break 
    

list_1 = []    
import csv
for i in range(len(data)):
    X_data = data[i].values()
    list_1.append(X_data)
with open("csvfile2.csv", "w") as output:
    writer = csv.writer(output , quoting=csv.QUOTE_ALL)
    writer.writerows(list_1)  
   
    
"""import nltk   
list_2 =[]
from textblob import TextBlob
file= pd.read_csv("C:\\Users\\Dimpy\\Desktop\\csvfile2.csv", encoding ="ISO-8859-1")
msg = (file.iloc[:, 1]).dropna()
for j in range(len(msg)):
    blob = TextBlob(str(msg.iloc[j]))
    x =list(blob.sentiment)
    list_2.append(x)"""
    
    
"""from textblob import TextBlob
import re

def clean_tweet(data):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data).split())

def analize_sentiment(data):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(data))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    # We create a column with the result of the analysis:
data['SA'] = np.array([ analize_sentiment(data) for data in data['data'] ])

# We display the updated dataframe with the new column:
display(data.head(100))

pos_tweets = [ data for index, data in enumerate(data['data']) if data['SA'][index] > 0]
neu_tweets = [ data for index, data in enumerate(data['data']) if data['SA'][index] == 0]
neg_tweets = [ data for index, data in enumerate(data['data']) if data['SA'][index] < 0]
print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['data'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['data'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['data'])))
"""
ID=[]
Message=[]
#df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
df = pd.DataFrame({'id': ID, 'message': Message})
df 
