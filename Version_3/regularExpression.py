from collections import defaultdict
import pandas as pd
import numpy as np
import re
import csv
f = open('/content/Dataset-version3.csv', 'w')
file_loc = "/content/Dataset-version2.xlsx"
data = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="A:C")
df = pd.DataFrame(data, columns= ['Package name','App name ','Review all'])
x=df[df['Review all'].str.contains('.*privacy*.|.*security*.|.*backup*.|.*permission*.|.*authenticate*.|.*login*.|.*credentials*.|.*encryption*.|.*decryption*.|.*risk*.|.*malware*.|.*attack*.|.*breach*.|.*exploit*.|.*firewall*.|.*virus*.|.*hacker*.|.*password*.')==True]
print(x)
x.to_csv('/content/Dataset-version3.csv')
     
