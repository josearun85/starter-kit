# Import the Twython class
from twython import Twython  
import json
import pandas as pd


# Credentials

creds = {"CONSUMER_KEY":"***", "CONSUMER_SECRET":"*****"}

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'trump',  
        'result_type': 'popular',
        'count': 25,
        'lang': 'en',
        }
		

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
df.sort_values(by='favorite_count', inplace=True, ascending=False)  
print df.head(15)  		
