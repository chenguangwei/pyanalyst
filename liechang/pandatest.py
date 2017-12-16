import  pandas as pd
import numpy as np
from pandas import Series,DataFrame
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj = obj.reindex(['a', 'b', '2', '1', 'e'], fill_value=0)
# print (obj)

# print('默认一维为数组:', np.arange(5))
# print('自定义起点一维数组:',np.arange(1, 5))
#
#
# print('二维数组:', np.arange(8).reshape((2, 4)))
#
#
# print(np.arange(60).reshape((3, 4, 5)))


# s = Series(['2012-12-01', '30/01/2012'])

name=['date','rate','comment']
df = pd.read_table('date_rate_comment.txt',encoding= 'utf-8',header=None,names=name,sep=',')

a = pd.to_datetime(df['date'])
print(a.value_counts())
