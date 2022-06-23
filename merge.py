import os

import pandas as pd

data = pd.DataFrame()
listdir = os.listdir()
for each in listdir:
    if each.endswith('.csv'):
        data = pd.concat([data, pd.read_csv(os.getcwd() + os.sep + each)], axis=0, ignore_index=True)
    elif each.endswith('.xlsx'):
        data = pd.concat([data, pd.read_excel(os.getcwd() + os.sep + each)], axis=0, ignore_index=True)
    elif each.endswith('.xls'):
        data = pd.concat([data, pd.read_excel(os.getcwd() + os.sep + each)], axis=0, ignore_index=True)
    elif each.endswith('.txt'):
        data = pd.concat([data, pd.read_csv(os.getcwd() + os.sep + each)], axis=0, ignore_index=True)
    else:
        print('error')
data.to_csv(os.getcwd() + os.sep + 'all.csv', index=False)