import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
nltk.download('punkt')
import warnings
warnings.filterwarnings("ignore")

def preprocess(text: str):
    
    stop_words = set(stopwords.words('english'))
    
    tokenizer = RegexpTokenizer(r'\w+')

    text = " ".join(tokenizer.tokenize(text))

    #print("w/o punctuation:", text)
    word_tokens = word_tokenize(text)
    
    #print("tokens:",  str(word_tokens))

    lower_case = [w.lower() for w in word_tokens]

    #print("lowercase: ",str(lower_case))
    filtered_sentence = [w for w in lower_case if not w in stop_words]
    #print("stop words:",str(filtered_sentence))
    #ps = PorterStemmer()

    #stemmed_text = [ps.stem(w) for w in filtered_sentence]
    #print("stemmed:",str(stemmed_text))

    return " ".join(filtered_sentence)


df=pd.read_csv('SO_data_cleared.csv')
df["title"] = df["title"].apply(preprocess)

df.to_csv("data_preprocessed_titles.csv")