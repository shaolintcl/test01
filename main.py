#-*-encoding:utf-8-*-

import pandas as pd

dic1 = {'aa':[1,2,3,4,5],'bb':['a','b','c','d','e']}

df_1 = pd.DataFrame(dic1)
print(df_1)

df_1['cc'] = df_1.apply(lambda x : True if x['bb']=='a' else False,axis=1)
print(df_1)

df_1.drop(df_1.index[df_1['cc']==False],inplace=True)
print(df_1)