import pandas as pd
import nltk
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

df = pd.read_csv("saved_tweets.csv")
df.columns = ['text','hastags','user','user_loc']


token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for i in range(0,df.shape[0]):
	text = df.loc[i,"text"]
	lowers = text.lower()
	no_punctuation = lowers.translate(None, string.punctuation)
	token_dict[i] = no_punctuation
        
#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

pdtf = pd.DataFrame( tfs.toarray())
pdtf.columns = tfidf.get_feature_names()

pdtf.to_csv("tfidf.csv")