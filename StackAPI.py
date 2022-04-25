#from stackapi import StackAPI
import requests
import json
import pandas as pd
import time
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

def requestsAPI():
    api_key='YqYacsm9i5b2gxBbdsQUxg(('
    i=1
    request_statement = "https://api.stackexchange.com/2.3/tags/python/faq?&site=stackoverflow&pagesize=100&page=" + str(i)+"&key="+api_key
    quota_remaining=10000
    questions=[]
    has_more=True
    while  quota_remaining>30 and has_more==True:       
        r=requests.get(request_statement)
        resp=json.loads(r.text)
        try:
            questions+=resp["items"]
            quota_remaining=resp["quota_remaining"]
            if resp["has_more"]!=True:
                has_more=False
            print("Processed page " + str(i) + ", question length: " + str(len(questions)))
            i+=1
        except:
            time.sleep(10)
    dfItem = pd.DataFrame.from_records(questions)
    dfItem.head(5)
    dfItem.to_csv("question_data.csv")
    

requestsAPI()