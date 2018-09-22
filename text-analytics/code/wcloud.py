# Python program to generate WordCloud 
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
 
# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
  
df = pd.read_csv("saved_tweets.csv", encoding ="latin-1") 
  
df.columns = ['text','hastags','user','user_loc']
  
comment_words = ' '
stopwords = set(STOPWORDS) 

print df.head()
  
# iterate through the csv file 
for val in df.text: 
      
    # typecaste each val to string 
    val = str(val) 
    print val
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    for words in tokens: 
		comment_words = comment_words + words + ' '
  
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.savefig('wcloud.png')  
#plt.show() 