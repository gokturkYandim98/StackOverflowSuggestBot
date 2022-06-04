import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np
import os

df=pd.read_csv("SO_Dataset/data_preprocessed.csv")

print("dataset's shape before filtering:",df.shape)
df_error = df[df["title"].str.contains('error',na=False)]
print("dataset's shape after filtering:",df_error.shape)
df_error = df_error.dropna(subset=["title"])
print("dataset's shape after dropping na's:",df_error.shape)
df_error.to_csv("SO_data_error_queries.csv")