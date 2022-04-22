#from stackapi import StackAPI
import requests
import json

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
    request_statement = "https://api.stackexchange.com/2.3/tags/python?site=stackoverflow&key="+api_key
    r = requests.get(request_statement)
    resp=json.loads(r.text)
    print(len(resp['items']))
    for quest in resp['items']:
        if 'title' not in quest or quest['is_answered'] == False:
            continue
        title = quest['title'] 
        print('Question :- {0}'.format(title))
        question_id = quest['question_id']
        print('Question ID :- {0}'.format(question_id))
        top_answer="https://api.stackexchange.com/2.3/questions/"+str(question_id)+"/answers/order=desc&sort=votes&key="+api_key
        if 'accepted_answer_id' in quest.keys():
            accepted_answer_id = quest['accepted_answer_id']
            print('Accepted Answer ID :- {0}'.format(accepted_answer_id))
        print("\n----------------------------------------------------------------\n")

requestsAPI()