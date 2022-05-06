import requests
import json
import pandas as pd
import time
from datetime import datetime
import numpy as np


def preprocess():
    df=pd.read_csv('data3.csv')