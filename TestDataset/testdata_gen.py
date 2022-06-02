# -*- coding: utf-8 -*-
"""testdata_gen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GxXtTqxu7QQNyQiD6K-cbkQIfT9lHEkW
"""

!pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git

from parrot import Parrot

parrot = Parrot()

import pandas as pd
from google.colab import drive
import json
drive.mount('/content/drive')

DATA_PATH = '/content/drive/MyDrive/CS48000-DesignPatterns/'

df = pd.read_csv (DATA_PATH+'SO_data_cleared.csv')

df = df.tail(73000)

df.shape

phrases = []
counter = 0

for i in range(len(df)):
  if "error" in df.iloc[i]["title"]:
    phrases.append(df.iloc[i]["title"])
    counter+=1
  if counter == 100:
    break

import pprint
pprint.pprint(phrases)

modified = {}
i = 0

for phrase in phrases:
  print("Input_phrase: ", phrase)
  paraphrases = parrot.augment(input_phrase=phrase)
  modified[i] = dict()
  modified[i]["Original"] = phrase
  modified[i]["Paraphrases"] = list()
  try:
    for paraphrase in paraphrases:
      modified[i]["Paraphrases"].append(paraphrase)
  except:
    continue
  i+=1

pprint.pprint(modified)

with open ("paraphrases.json","w") as file:
  json.dump(modified, file,indent=4)

from google.colab import files
files.download("paraphrases.json")