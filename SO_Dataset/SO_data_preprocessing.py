import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np
import os
#from hurry.filesize import size




df=pd.read_csv("SO_data.csv")

file_size = os.stat('SO_data.csv')
print("Size of the file before preprocessing:", "{:.2f}".format(file_size.st_size/(1024*1024)),"MB\n")

drop_cols=['protected_date', 'bounty_amount',
       'bounty_closes_date', 'migrated_from', 'locked_date', 'migrated_to',
       'community_owned_date']
       
print("shape of the data before dropping the unnecessary columns:",df.shape)
df=df.drop(drop_cols, axis=1)
print("shape of the data after dropping the unnecessary columns:",df.shape)

df.drop_duplicates(subset ="question_id", keep = False, inplace = True)
print("shape of the data after dropping the duplicates:",df.shape)

df = df[df.is_answered == True]
print("shape of the data after dropping the unanswered:",df.shape)

df.to_csv("SO_data_cleared.csv")

file_size2 = os.stat('SO_data_cleared.csv')
print("\nSize of the file after preprocessing:","{:.2f}".format(file_size2.st_size/(1024*1024)),"MB")