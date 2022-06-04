import pandas as pd
from datetime import datetime
import numpy as np

df=pd.read_csv('SO_error_titles_answer_data.csv')

question = input("Enter your question about python: ")

#here send question to the model    question 

question_id1=62847518 #id coming from the model
title1="valueerror shapes none 2 none 1 incompatible" #title coming from the model
isValid1=True
isValid2=True
question_id2=23234 #id coming from the model
title2="xxxx"


if isValid1:
    print("This question sounds similar to yours:",title1)
    answers=df[df["question_id"]==question_id1]
    print("Links to answers to this question:")
    counter=1
    for index, row in answers.iterrows():
        print(str(counter)+".",row["link"] )
        counter+=1
elif isValid2:
    print("This question sounds similar to yours:",title2)
    answers=df[df["question_id"]==question_id2]
    print("Links to answers to this question:")
    counter=1
    for index, row in answers.iterrows():
        print(str(counter)+".",row["link"] )
        counter+=1
else:
    print("We couldn't find any matches :(")
    