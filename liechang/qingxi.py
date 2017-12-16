import pandas as pd
import matplotlib.pyplot as plt
name=['date','rate','comment']
df = pd.read_table('date_rate_comment.txt',encoding= 'utf-8',header=None,names=name,sep=',')
# print(df['date'])
df['date'] = pd.to_datetime(df['date'])

print(df['comment'].to_string(index=False))


with open("3.txt", 'w') as word:
    word.write(df['comment'].to_string(index=False))