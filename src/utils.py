"""
Small utitlity file to work in this specific analysis
"""

import pandas as pd

def convert_txt_df(path):
    txt_data = ''
    print('Reading Text File')
    with open(path, 'r') as f:
        txt_data = f.readlines()
    #iterate and convert
    print('Removing new line and "|"')
    txt_data = [[spelling.replace('\n', '') for spelling in word.split('|')] for word in txt_data]
    cols, data = txt_data[0], txt_data[1:]
    
    #pd
    print('Convering to data frame')
    df = pd.DataFrame(data, columns=cols)
    
    # print(df.head())
    return df, cols

# convert_txt_df('../data/MachineLearningRating_v3.txt')

def convert_str_int(df, col):
    df[col] = pd.to_numeric(df[col])
    
    
def to_numeric(df, columns):
    for column in cols[:]:
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            df[column] = df[column]
    return df

