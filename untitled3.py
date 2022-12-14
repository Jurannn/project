# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emSDEA6JtfVv7RPUpOL6X1YJqH5oVK_A

#**데이터 개요
"""

from google.colab import drive
drive.mount("/content/gdrive")

import numpy as np
import pandas as pd

data_path_train_input = '/content/gdrive/MyDrive/open/train_input/'
data_path_train_target = '/content/gdrive/MyDrive/open/train_target/'
data_path_test_input = '/content/gdrive/MyDrive/open/test_input/'
data_path_test_target = '/content/gdrive/MyDrive/open/test_target/'
data_path_submission = '/content/gdrive/MyDrive/open/sample_submission/'

train_input1 = pd.read_csv(data_path_train_input + 'CASE_01.csv')
train_target1 = pd.read_csv(data_path_train_target + 'CASE_01.csv')
test_input1 = pd.read_csv(data_path_test_input + 'TEST_01.csv')
test_target1 = pd.read_csv(data_path_test_target + 'TEST_01.csv')
submission1 = pd.read_csv(data_path_submission + 'TEST_01.csv')

train_input1.shape #train 데이터의 피쳐 수 : 38개 --> 1분간격 관측

test_input1.shape #train 데이터와 test 데이터 피쳐 개수 동일

train_input1.head()

train_input1.tail()

test_input1.head()

train_input1.info() #피쳐확인 -> 데이터 결측치 존재

train_target1.shape #train 데이터의 피쳐 수 : 2개 --> 1일간격 관측

test_target1.shape

train_target1.head()

test_target1.head()

test_input1.info()

"""# **traget과 input데이터 병합하기

datetime 피쳐 처리
"""

#데이터 피쳐 생성
train_input1['date'] = train_input1['시간'].apply(lambda x: x.split()[0])
#월, 일 피쳐 생성
train_input1['month'] = train_input1['시간'].apply(lambda x: x.split()[0].split('-')[1])
train_input1['day'] = train_input1['시간'].apply(lambda x: x.split()[0].split('-')[2])
#시, 분 피쳐 생성
train_input1['hour'] = train_input1['시간'].apply(lambda x: x.split()[1].split(':')[0])
train_input1['minute'] = train_input1['시간'].apply(lambda x: x.split()[1].split(':')[1])

train_input1.head()

train_input1_mean = train_input1.groupby("date").mean()
train_input1_mean

train_target1['date'] = train_target1['시간'].apply(lambda x: x.split()[0])

train_target1.head()



train1 = pd.merge(train_target1, train_input1_mean, how = 'outer', on = 'date')
train1.head()
#3/18과 2/17은 제거해야함



"""#**데이터 시각화"""

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', size = 15)
sns.displot(train1['rate'])

#타겟값인 rate가 정규분포를 따르지 않으므로 로그 변환
sns.displot(np.log(train1['rate']))

train1.shape

dtrain1 = train1.dropna()
dtrain1.head()

mpl.rc('font', size = 10)
mpl.rc('axes', titlesize = 10)
figure, axes = plt.subplots(nrows = 13, ncols = 3)
plt.tight_layout()
figure.set_size_inches(30,30)



sns.regplot(x='내부온도관측치', y = 'rate', data = dtrain1, ax=axes[0,0])
sns.regplot(x='내부습도관측치', y = 'rate', data = dtrain1, ax=axes[0,1])
sns.regplot(x='CO2관측치', y = 'rate', data = dtrain1, ax=axes[0,2])
sns.regplot(x='EC관측치', y = 'rate', data = dtrain1, ax=axes[1,0])
sns.regplot(x='펌프상태', y = 'rate', data = dtrain1, ax=axes[1,1])
sns.regplot(x='펌프작동남은시간', y = 'rate', data = dtrain1, ax=axes[1,2])
sns.regplot(x='최근분무량', y = 'rate', data = dtrain1, ax=axes[2,0])
sns.regplot(x='일간누적분무량', y = 'rate', data = dtrain1, ax=axes[2,1])
sns.regplot(x='냉방상태', y = 'rate', data = dtrain1, ax=axes[2,2])
sns.regplot(x='냉방작동남은시간', y = 'rate', data = dtrain1, ax=axes[3,0])
sns.regplot(x='난방상태', y = 'rate', data = dtrain1, ax=axes[3,1])
sns.regplot(x='난방작동남은시간', y = 'rate', data = dtrain1, ax=axes[3,2])
sns.regplot(x='내부유동팬작동남은시간', y = 'rate', data = dtrain1, ax=axes[4,0])
sns.regplot(x='외부환기팬상태', y = 'rate', data = dtrain1, ax=axes[4,1])
sns.regplot(x='외부환기팬작동남은시간', y = 'rate', data = dtrain1, ax=axes[4,2])
sns.regplot(x='화이트 LED상태', y = 'rate', data = dtrain1, ax=axes[5,0])
sns.regplot(x='화이트 LED작동남은시간', y = 'rate', data = dtrain1, ax=axes[5,1])
sns.regplot(x='화이트 LED동작강도', y = 'rate', data = dtrain1, ax=axes[5,2])
sns.regplot(x='레드 LED상태', y = 'rate', data = dtrain1, ax=axes[6,0])
sns.regplot(x='레드 LED작동남은시간', y = 'rate', data = dtrain1, ax=axes[6,1])
sns.regplot(x='레드 LED동작강도', y = 'rate', data = dtrain1, ax=axes[6,2])
sns.regplot(x='블루 LED상태', y = 'rate', data = dtrain1, ax=axes[7,0])
sns.regplot(x='블루 LED작동남은시간', y = 'rate', data = dtrain1, ax=axes[7,1])
sns.regplot(x='블루 LED동작강도', y = 'rate', data = dtrain1, ax=axes[7,2])
sns.regplot(x='카메라상태', y = 'rate', data = dtrain1, ax=axes[8,0])
sns.regplot(x='냉방온도', y = 'rate', data = dtrain1, ax=axes[8,1])
sns.regplot(x='난방온도', y = 'rate', data = dtrain1, ax=axes[8,2])
sns.regplot(x='기준온도', y = 'rate', data = dtrain1, ax=axes[9,0])
sns.regplot(x='난방부하', y = 'rate', data = dtrain1, ax=axes[9,1])
sns.regplot(x='냉방부하', y = 'rate', data = dtrain1, ax=axes[9,2])
sns.regplot(x='총추정광량', y = 'rate', data = dtrain1, ax=axes[10,0])
sns.regplot(x='백색광추정광량', y = 'rate', data = dtrain1, ax=axes[10,1])
sns.regplot(x='적색광추정광량', y = 'rate', data = dtrain1, ax=axes[10,2])
sns.regplot(x='청색광추정광량', y = 'rate', data = dtrain1, ax=axes[10,3])

