# -*- coding: utf-8 -*-
"""221122.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11KTrg1gADwNkQMGf1npzPbs-S2SqaCTg
"""

import numpy as np
import pandas as pd
import os
import datetime
from datetime import date
import seaborn as sns
import plotly.express as px

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

from google.colab import drive
drive.mount('/content/drive')

import os
os.getcwd()

os.chdir('/content/drive/MyDrive/betabrain/selecto')
mis1 = pd.read_excel("./MIS/MIS01.xlsx")
file_list = ["MIS0"+str(i)+".xlsx" for i in range(1,10)]
print(file_list)

file_list = ["MIS0"+str(i)+".xlsx" for i in range(1,10)]
#mis1 = pd.read_excel("./MIS/MIS0"+str(1)+".xlsx")
mis = []
for i in range(len(file_list)):
  mis.append(pd.read_excel("./MIS/"+ file_list[i]))

for i in range(len(mis)):
  print(mis[i].shape)
  mis[i]["month"] = i + 1

df_mis = pd.concat(mis)

df_reg = df_mis.groupby(['지역1','month']).size()

df_reg = df_reg.reset_index()
df_reg = df_reg.rename(columns={0: "cnt"})

df_reg

v = []
ic = []
# 비율 삽입
s = sum(df_reg["cnt"])
for i in df_reg["cnt"]:
    v.append((i/s)*100)
    ic.append(0)
df_reg["비율"] = v
df_reg["증감"] = ic

lst = []
for i in df_reg["month"]:
    if i not in lst:
        lst.append(i)

ch = []
for i in lst:
    lst_1 = list(df_reg[df_reg["month"]==i]["지역1"])
    for j in lst_1:
        k = df_reg[df_reg["month"]==i]
        k1 = df_reg[df_reg["month"]==i]
        t = k[k["지역1"]==j]
        t1 = k1[k1["지역1"]==j]
        if len(t) > 0 and len(t1) > 0:
            ch2 = (t["비율"].values[0]-t1["비율"].values[0])*100/(t1["비율"].values[0])
            ch.append(ch2)
        else:
            ch.append(0)

fig = px.treemap(df_reg, path=[px.Constant("월 별 지역"),'month', "지역1"], values = '비율',
                 color='비율',
                color_continuous_scale='bluyl',
                hover_data = {"증감":':.2p'}
                )
fig.data[0].texttemplate = "%{label}<br>증감:%{customdata[0]:.2f}%<br>Percent:%{value:.2f}%"
fig.show()

"""## FIS"""

os.chdir('/content/drive/MyDrive/betabrain/selecto')
fis = pd.read_excel("./MIS/FIS_new.xlsx")

fis_grade = fis.groupby(['운영','Unnamed: 92']).size()

fis_grade = fis_grade.reset_index()

fis_grade = fis_grade.rename(columns={0: "cnt"})

fis_grade

v = []
ic = []
# 비율 삽입
s = sum(fis_grade["cnt"])
for i in fis_grade["cnt"]:
    v.append((i/s)*100)
    ic.append(0)
fis_grade["비율"] = v
fis_grade["증감"] = ic

lst = []
for i in fis_grade["운영"]:
    if i not in lst:
        lst.append(i)

ch = []
for i in lst:
    lst_1 = list(fis_grade[fis_grade["운영"]==i]["Unnamed: 92"])
    for j in lst_1:
        k = fis_grade[fis_grade["운영"]==i]
        k1 = fis_grade[fis_grade["운영"]==i]
        t = k[k["Unnamed: 92"]==j]
        t1 = k1[k1["Unnamed: 92"]==j]
        if len(t) > 0 and len(t1) > 0:
            ch2 = (t["비율"].values[0]-t1["비율"].values[0])*100/(t1["비율"].values[0])
            ch.append(ch2)
        else:
            ch.append(0)

fig = px.treemap(fis_grade, path=[px.Constant("운영 별 등급"),'운영', "Unnamed: 92"], values = '비율',
                 color='비율',
                color_continuous_scale='bluyl',
                hover_data = {"증감":':.2p'}
                )
fig.data[0].texttemplate = "%{label}<br>증감:%{customdata[0]:.2f}%<br>Percent:%{value:.2f}%"
fig.show()

"""3.0(폐점)의 경우 D등급이 가장 많음

1.0(영업)의 경우에도 D등급이 가장 많음

> 폐장한 매장과 영업한 매장 모두 D등급이 많으므로, 영업이익등급에 따라 폐장/영업 여부를 판단하기 어려움

"""

fis_br = fis.groupby(['운영','Unnamed: 91']).size()

fis_br = fis_br.reset_index()
fis_br = fis_br.rename(columns={0: "cnt"})
fis_br

v = []
ic = []
# 비율 삽입
s = sum(fis_br["cnt"])
for i in fis_br["cnt"]:
    v.append((i/s)*100)
    ic.append(0)
fis_br["비율"] = v
fis_br["증감"] = ic

lst = []
for i in fis_br["운영"]:
    if i not in lst:
        lst.append(i)

ch = []
for i in lst:
    lst_1 = list(fis_br[fis_br["운영"]==i]["Unnamed: 91"])
    for j in lst_1:
        k = fis_br[fis_br["운영"]==i]
        k1 = fis_br[fis_br["운영"]==i]
        t = k[k["Unnamed: 91"]==j]
        t1 = k1[k1["Unnamed: 91"]==j]
        if len(t) > 0 and len(t1) > 0:
            ch2 = (t["비율"].values[0]-t1["비율"].values[0])*100/(t1["비율"].values[0])
            ch.append(ch2)
        else:
            ch.append(0)

fig = px.treemap(fis_br, path=[px.Constant("운영 별 흑자/적자"),'운영', "Unnamed: 91"], values = '비율',
                 color='비율',
                color_continuous_scale='bluyl',
                hover_data = {"증감":':.2p'}
                )
fig.data[0].texttemplate = "%{label}<br>증감:%{customdata[0]:.2f}%<br>Percent:%{value:.2f}%"
fig.show()

"""3.0(폐점)의 경우 적자 비율이 37.35%

1.0(영업)의 경우 적자 비율이 16.12%

> 폐장한 매장의 경우 적자 비율이 높은 반면, 영업 중인 매장의 경우 적자 비율이 낮다. 따라서 흑자/적자를 기준으로 매장의 폐장 여부를 예측할 수 있다.

"""

fis_location = fis.groupby(['운영','지역1']).size()

fis_location = fis_location.reset_index()
fis_location = fis_location.rename(columns={0: "cnt"})
fis_location

v = []
ic = []
# 비율 삽입
s = sum(fis_location["cnt"])
for i in fis_location["cnt"]:
    v.append((i/s)*100)
    ic.append(0)
fis_location["비율"] = v
fis_location["증감"] = ic

lst = []
for i in fis_location["운영"]:
    if i not in lst:
        lst.append(i)

ch = []
for i in lst:
    lst_1 = list(fis_location[fis_location["운영"]==i]["지역1"])
    for j in lst_1:
        k = fis_location[fis_location["운영"]==i]
        k1 = fis_location[fis_location["운영"]==i]
        t = k[k["지역1"]==j]
        t1 = k1[k1["지역1"]==j]
        if len(t) > 0 and len(t1) > 0:
            ch2 = (t["비율"].values[0]-t1["비율"].values[0])*100/(t1["비율"].values[0])
            ch.append(ch2)
        else:
            ch.append(0)

fig = px.treemap(fis_location, path=[px.Constant("운영 별 지역"),'운영', "지역1"], values = '비율',
                 color='비율',
                color_continuous_scale='bluyl',
                hover_data = {"증감":':.2p'}
                )
fig.data[0].texttemplate = "%{label}<br>증감:%{customdata[0]:.2f}%<br>Percent:%{value:.2f}%"
fig.show()

"""3.0(폐점) 비율과 1.0(영업)의 비율을 비교했을 떄, 3.0(폐점)의 비율이 유의미한 지역 : 서울, 인천, 부산

3.0(폐점) 비율과 1.0(영업)의 비율을 비교했을 떄, 1.0(영업)의 비율이 유의미한 지역 : 충남

> 지역 별 폐장/영업 영향이 존재하는 것으로 보임

"""

fis_mark = fis.groupby(['운영','상권']).size()

fis_mark = fis_mark.reset_index()
fis_mark = fis_mark.rename(columns={0: "cnt"})
fis_mark

v = []
ic = []
# 비율 삽입
s = sum(fis_mark["cnt"])
for i in fis_mark["cnt"]:
    v.append((i/s)*100)
    ic.append(0)
fis_mark["비율"] = v
fis_mark["증감"] = ic

lst = []
for i in fis_mark["운영"]:
    if i not in lst:
        lst.append(i)

ch = []
for i in lst:
    lst_1 = list(fis_mark[fis_mark["운영"]==i]["상권"])
    for j in lst_1:
        k = fis_mark[fis_mark["운영"]==i]
        k1 = fis_mark[fis_mark["운영"]==i]
        t = k[k["상권"]==j]
        t1 = k1[k1["상권"]==j]
        if len(t) > 0 and len(t1) > 0:
            ch2 = (t["비율"].values[0]-t1["비율"].values[0])*100/(t1["비율"].values[0])
            ch.append(ch2)
        else:
            ch.append(0)

fig = px.treemap(fis_mark, path=[px.Constant("운영 별 상권"),'운영', "상권"], values = '비율',
                 color='비율',
                color_continuous_scale='bluyl',
                hover_data = {"증감":':.2p'}
                )
fig.data[0].texttemplate = "%{label}<br>증감:%{customdata[0]:.2f}%<br>Percent:%{value:.2f}%"
fig.show()

"""
> 상권 별 폐장/영업 영향이 존재하지 않는 것으로 보임"""

