import json
import pandas as pd
from pandas import json_normalize   
with open('data3.json') as f:
    data = json.load(f) 
df = json_normalize(data)
print(df)