import pandas as pd
import nltk
#nltk.download('stopwords')
import string
import re
import sys

from nltk.corpus import stopwords

#make a list of english stopwords
stopwords = nltk.corpus.stopwords.words("english")

#read csv file
df = pd.read_csv('eclass_all_with_sentiment.csv', on_bad_lines='skip')

#set to lower case letters
df = df.apply(lambda x: x.astype(str).str.lower())

for col in df:
  #remove stopwords
  df[col] = df[col].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
  #remove URLs
  df[col] = df[col].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
  #remove punctuation
  df[col] = df[col].str.translate(str.maketrans('','',string.punctuation))
  
#remove emojies
df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))


nf = pd.DataFrame(df, columns = df.columns)
nf.to_csv('eclass_all_with_sentiment_modified.csv', index=False)