#from stackapi import StackAPI
import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np
api_key='YqYacsm9i5b2gxBbdsQUxg(('
"""
def libraryAPI():
    SITE = StackAPI('stackoverflow')
    SITE.max_pages=2
    SITE.page_size=25
    questions = SITE.fetch('questions',order='desc',tagged='python',site='stackoverflow',key=api_key)

    print(len(questions['items']))

    for quest in questions['items']:
        if 'title' not in quest or quest['is_answered'] == False:
            continue
        title = quest['title'] 
        print('Question :- {0}'.format(title))
        question_id = quest['question_id']
        print('Question ID :- {0}'.format(question_id))
        top_answer = SITE.fetch('questions/' + str(question_id) + '/answers', order = 'desc', sort='votes',key=api_key)
        if 'accepted_answer_id' in quest.keys():
            accepted_answer_id = quest['accepted_answer_id']
        print('Accepted Answer ID :- {0}'.format(accepted_answer_id))
        print("\n----------------------------------------------------------------\n")"""

def f(d):
    if pd.isnull(d)==False:
        d=pd.to_datetime(int(d), utc=True, unit='ms')
def requestsAPI():
    #api_key="QjDXYYOi0oHOU)LwtDxO*Q(("
    i=1
    request_statement = "https://api.stackexchange.com/2.3/questions?&tagged=python&site=stackoverflow&pagesize=100&page=" + str(i)+"&key="+api_key
    quota_remaining=10000
    questions=[]
    has_more=True
    while  quota_remaining>0 and has_more==True:       
        request_statement = "https://api.stackexchange.com/2.3/questions?&tagged=python&site=stackoverflow&pagesize=100&page=" + str(i)+"&key="+api_key
        r=requests.get(request_statement)
        resp=json.loads(r.text)
        try:
            questions+=resp["items"]
            quota_remaining=resp["quota_remaining"]
            if resp["has_more"]!=True:
                has_more=False
            print("Processed page " + str(i) + ", question length: " + str(len(questions)))
            print("unique questions:",len(np.unique(list([v['question_id'] for v in questions]))))
            i+=1
        except:
            if r.status_code==443:
                break
            time.sleep(10)

    df = pd.DataFrame.from_records(questions)
    try:
        htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
        for code in htmlCodes:
            df["title"]=[r.replace(code[1], code[0]) for r in df["title"]]
        
        df = df.drop(["owner", "last_edit_date","content_license", "closed_date", "closed_reason"], axis = 1)
        
        dates = ["last_activity_date","creation_date"]
        
        for col in dates:
            df=df.astype({col:str})
            for i, r in enumerate(df[col]):  
                if r!="nan":
                    r1=datetime.fromtimestamp(float(r)).strftime('%Y-%m-%d')
                    df.at[i, col] = r1 
        df.to_csv("SO_data.csv")
    except:
    #df=df.drop_duplicates()
        df.to_csv("SO_data.csv")
    print(df.head(5))

requestsAPI()