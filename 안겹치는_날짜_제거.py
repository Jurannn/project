# -*- coding: utf-8 -*-
"""0000000안겹치는 날짜 제거

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H-3KaO_QSfFqEJwhtjqK6HCbTGFUAHrd

# import
"""

# 구글 드라이브 연결
from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn import preprocessing

#train_target
number=range(1,10)
li=[]
for num in number:
    path='/content/drive/MyDrive/AI_competition/train_target/CASE_0%d.csv'%num
    df = pd.read_csv(path, index_col=None, header=0)
    df['case']=''
    df=df.replace('','CASE_0%d'%num)
    li.append(df)
frame3=pd.concat(li,axis=0,ignore_index=True)

number1=range(10,59)
li=[]
for num in number1:
    path='/content/drive/MyDrive/AI_competition/train_target/CASE_%d.csv'%num
    df = pd.read_csv(path, index_col=None, header=0)
    df['case']=''
    df=df.replace('','CASE_%d'%num)
    li.append(df)
frame4=pd.concat(li,axis=0,ignore_index=True)

train_target=pd.concat([frame3,frame4],axis=0)

path='/content/drive/MyDrive/AI_competition/train_input_final.csv'
train_input = pd.read_csv(path, index_col=None, header=0)

train_target.head()



"""# train

## date 변수 조정
"""

#########train_input date 조정

train_input['date']=train_input['시간'].apply(lambda x:x.split()[0])

train_input['date'] = pd.DatetimeIndex(train_input['date']) + timedelta(days=1)

train_input['date'] = train_input['date'].astype(str)

a = set(train_input[train_input['case'] == 'CASE_01']['date'])
a

#########train_target date 조정

train_target['date']=train_target['시간'].apply(lambda x:x.split()[0])
train_target['date'] = train_target['date'].astype(str)





train_target['date'] = train_target['date'].astype(str)

train_target.head()

"""## train input과 target차집합"""

empty = set()

  for num in range(1,10):
    a = set(train_target[train_target['case'] == 'CASE_%0d'%num]['date'])
    b = set(train_input[train_input['case'] == 'CASE_%0d'%num]['date'])
    if (a|b) - (a&b) == empty:
      np.NaN
    else:
      print(f"%0d번 케이스는 공집합이 아니다 : {(a|b) - (a&b)} \n target에만 있음 : {a-b} \n input에만 있음{b-a}"%num)

empty = set()

for num in range(10,59):
  a = set(train_target[train_target['case'] == 'CASE_%d'%num]['date'])
  b = set(train_input[train_input['case'] == 'CASE_%d'%num]['date'])
  if (a|b) - (a&b) == empty:
    np.NaN
  else:
    print(f"%d번 케이스는 공집합이 아니다 : {(a|b) - (a&b)} \n target에만 있음 : {a-b} \n input에만 있음{b-a}"%num)



"""## train target 일부 행 제거

### train target 인덱스 번호 찾기 후 안겹치는 날짜 제거
"""

#case 38
tt38 = train_target[train_target['case'] == 'CASE_38']

print(tt38[tt38['date'] == '2022-03-06'].index)
print(tt38[tt38['date'] == '2022-03-07'].index)
print(tt38[tt38['date'] == '2022-03-08'].index)
print(tt38[tt38['date'] == '2022-03-10'].index)
print(tt38[tt38['date'] == '2022-03-11'].index)
print(tt38[tt38['date'] == '2022-03-13'].index)
print(tt38[tt38['date'] == '2022-03-14'].index)

#case 41
tt41 = train_target[train_target['case'] == 'CASE_41']

print(tt41[tt41['date'] == '2022-03-24'].index)
print(tt41[tt41['date'] == '2022-03-25'].index)
print(tt41[tt41['date'] == '2022-03-26'].index)
print(tt41[tt41['date'] == '2022-03-27'].index)
print(tt41[tt41['date'] == '2022-03-28'].index)
print(tt41[tt41['date'] == '2022-03-29'].index)
print(tt41[tt41['date'] == '2022-03-30'].index)

#case 44
tt44 = train_target[train_target['case'] == 'CASE_44']

print(tt44[tt44['date'] == '2022-03-24'].index)
print(tt44[tt44['date'] == '2022-03-25'].index)
print(tt44[tt44['date'] == '2022-03-26'].index)
print(tt44[tt44['date'] == '2022-03-27'].index)
print(tt44[tt44['date'] == '2022-03-28'].index)
print(tt44[tt44['date'] == '2022-03-29'].index)
print(tt44[tt44['date'] == '2022-03-30'].index)

#case 47
tt47 = train_target[train_target['case'] == 'CASE_47']

print(tt47[tt47['date'] == '2022-04-09'].index)

df2 = df.drop(columns=df.columns[[0,2]])

[944, 942, 943, 950, 949, 946, 947, 
                                  1032, 1036, 1030, 1035, 1033, 1034, 1031,
                                  1093, 1097, 1091, 1096, 1094, 1095, 1092, 1198])
train_target

train_target = train_target.drop([944, 942, 943, 950, 949, 946, 947, 
                                  1032, 1036, 1030, 1035, 1033, 1034, 1031,
                                  1093, 1097, 1091, 1096, 1094, 1095, 1092, 1198].index)
train_target

train_target = train_target.drop(['date'], axis = 1)

"""##train input 일부 행 제거 및 스케일링

### train input 인덱스 번호 찾기 후 안겹치는 날짜 제거
"""

#case 43
ti43 = train_input[train_input['case'] == 'CASE_43']

index43 = ti43[ti43['date'] == '2022-03-22'].index

train_input = train_input.drop(index43)

"""### train input스케일링"""

#파이썬 데이터프레임 minmaxscaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

column_names_to_not_normalize = ['시간', 'case', 'date']
column_names_to_normalize = [x for x in list(train_input) if x not in column_names_to_not_normalize ]
x = train_input[column_names_to_normalize].values

mn_X = MinMaxScaler()
x_scaled = mn_X.fit_transform(x)

train_input_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = train_input.index)
train_input[column_names_to_normalize] = train_input_temp

train_input

train_input = train_input.drop(['date'], axis = 1)
train_input.head()

#train_input.to_csv("train_input_scaled.csv", index = False)







"""#test

### test 차집합
"""

#test_input
number=range(1,7)
li=[]
for num in number:
    path='/content/drive/MyDrive/AI_competition/test_input/TEST_0%d.csv'%num
    df = pd.read_csv(path, index_col=None, header=0)
    df['case']=''
    df=df.replace('','CASE_0%d'%num)
    li.append(df)
test_input=pd.concat(li,axis=0,ignore_index=True)
#test_target
number=range(1,7)
li=[]
for num in number:
    path='/content/drive/MyDrive/AI_competition/test_target/TEST_0%d.csv'%num
    df = pd.read_csv(path, index_col=None, header=0)
    df['case']=''
    df=df.replace('','CASE_0%d'%num)
    li.append(df)
test_target=pd.concat(li,axis=0,ignore_index=True)

#test_input date 조정

test_input['date']=test_input['시간'].apply(lambda x:x.split()[0])

test_input['date'] = pd.DatetimeIndex(test_input['date']) + timedelta(days=1)

test_input['date'] = test_input['date'].astype(str)

#test_input date 조정

test_target['date']=test_target['시간'].apply(lambda x:x.split()[0])

test_target['date'] = test_target['date'].astype(str)



empty = set()

  for num in range(1,7):
    a = set(test_target[test_target['case'] == 'CASE_%0d'%num]['date'])
    b = set(test_input[test_input['case'] == 'CASE_%0d'%num]['date'])
    if (a|b) - (a&b) == empty:
      print(np.NaN)
    else:
      print(f"%0d번 케이스는 공집합이 아니다 : {(a|b) - (a&b)} \n target에만 있음 : {a-b} \n input에만 있음{b-a}"%num)

"""###test 스케일링"""

#파이썬 데이터프레임 minmaxscaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

column_names_to_not_normalize = ['시간', 'case', 'date']
column_names_to_normalize = [x for x in list(test_input) if x not in column_names_to_not_normalize ]
x = test_input[column_names_to_normalize].values

mn_X = MinMaxScaler()
x_scaled = mn_X.fit_transform(x)

test_input_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = test_input.index)
test_input[column_names_to_normalize] = test_input_temp

test_input

test_input.to_csv("test_input_scaled.csv", index = False)



import torch
import numpy
time_series = input_df[(input_df1[idx]*(idx)):input_df1[idx]*(idx+1)].values
                time_series = torch.from_numpy(time_series )
                self.data_list.append(torch.tensor((time_series)))



