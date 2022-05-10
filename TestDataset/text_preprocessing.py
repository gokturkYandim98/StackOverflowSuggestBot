import json
import os
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
    for word in ["python","traceback","most","recent","last","call"]:
        stop_words.add(word)
    
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

path = r"C:\Users\samil\Desktop\StackOverflowSuggestBot\TestDataset"

os.chdir(path)
with open ("test_data.json") as file:
    df = json.load(file)
    file.close()

for key in df:
    df[key]["errorType"]= preprocess(df[key]["errorType"])
    df[key]["traceback"]= preprocess(df[key]["traceback"])

with open ("preprocessed_test_data.json","w") as file:
    json.dump(df, file, indent=4)
    file.close()