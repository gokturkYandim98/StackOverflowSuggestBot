from stackapi import StackAPI
import pandas as pd

SITE = StackAPI('stackoverflow')
SITE.max_pages=10000
SITE.page_size=50
SITE.key='YqYacsm9i5b2gxBbdsQUxg(('
questions = SITE.fetch('questions',order='desc',tagged='python',site='stackoverflow')

print(len(questions['items']))
dfItem = pd.DataFrame.from_records(questions['items'])
dfItem.head(5)
dfItem.to_csv("data.csv")