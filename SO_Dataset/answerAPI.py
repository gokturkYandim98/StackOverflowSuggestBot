import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np
api_key='YqYacsm9i5b2gxBbdsQUxg(('

"""{
      "owner": {
        "account_id": 5149286,
        "reputation": 286317,
        "user_id": 4124317,
        "user_type": "registered",
        "accept_rate": 78,
        "profile_image": "https://i.stack.imgur.com/wsHAV.png?s=256&g=1",
        "display_name": "ImportanceOfBeingErnest",
        "link": "https://stackoverflow.com/users/4124317/importanceofbeingernest"
      },
      "is_accepted": true,
      "score": 4,
      "last_activity_date": 1561129630,
      "creation_date": 1561129630,
      "answer_id": 56706020,
      "question_id": 56704699,
      "content_license": "CC BY-SA 4.0"
    },"""


def requestsAPI():
    #api_key="QjDXYYOi0oHOU)LwtDxO*Q(("
    quota_remaining=10000
    answers=[]
    answers_count={} #dict to have record of answer count for each question
    questions=[]
    df=pd.read_csv('SO_Dataset\SO_data_error_queries.csv')
    groups=[]
    group_total=0
    current_group=[]
    for index, row in df.iterrows():
         group_total+=row["answer_count"]
         if group_total<31:
             current_group.append(str(row["question_id"]))
         else:
            group_total=row["answer_count"]
            groups.append(current_group)
            current_group=[str(row["question_id"])]

    for group in groups:        
        que = ";".join(group)
        request_statement = "https://api.stackexchange.com/2.3/questions/{}/answers?order=desc&filter=withbody&sort=votes&site=stackoverflow&key=".format(que)+api_key
        r=requests.get(request_statement)
        resp=json.loads(r.text)
        try:
            quota_remaining=resp["quota_remaining"]
            for item in resp["items"]:
                    #create a new dict including necessary columns of the answer
                item_new={
                        "is_accepted": item["is_accepted"],
                        "score": item["score"],
                        "creation_date": item["creation_date"],
                        "answer_id":item["answer_id"],
                        "question_id": item["question_id"],
                        "body": item["body"],
                        "link": "https://stackoverflow.com/a/{}".format(item["answer_id"])
                    }
                qid=item_new["question_id"]
                if qid in list(answers_count.keys()):
                        #if there are already 3 answers, don't put it in.
                    if answers_count[qid]<3:
                        answers.append(item_new)
                        answers_count[qid]+=1
                else:
                    answers.append(item_new)
                    answers_count[qid]=1
            print("Number of answer sets processed: " + str(len(answers)))
        except:
            if r.status_code==443:
                break
            time.sleep(10)
        print("Remaining request quota:",quota_remaining,"\n")
        #questions=[]

    df2=pd.DataFrame.from_dict(answers)

    try:
        df=df2.astype({"creation_date":str})
        for i, r in enumerate(df["creation_date"]):  
            if r!="nan":
                r1=datetime.fromtimestamp(float(r)).strftime('%Y-%m-%d')
                df.at[i, "creation_date"] = r1 
        df.to_csv("SO_error_titles_answer_data.csv")
    except:
    #df=df.drop_duplicates()
        df.to_csv("SO_error_titles_answer_data.csv")
    print(df.head(5))
requestsAPI()