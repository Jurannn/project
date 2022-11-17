import numpy as np
import pandas as pd


mis1 = pd.read_excel(r"C:\Users\USER\Desktop\betabrain\MIS\MIS01.xlsx")
mis2 = pd.read_excel(r"C:\Users\USER\Desktop\betabrain\MIS\MIS02.xlsx")
mis1.iloc[:,1]
mis2.iloc[:,1]

#set(mis1.iloc[:,1]) - set(mis2.iloc[:,1])
#set(mis2.iloc[:,1]) - set(mis1.iloc[:,1])
#set()
price1 = mis1.iloc[:,13:44].T
price1 = price1.reset_index()
price1 = price1.T


#%% 길이 같은 경우
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
idx111 = price1.loc['index']
query111 = price1.iloc[4]
query112 = price1.iloc[5]

path11 = dtw.warping_path(query111, query112)
dtwvis.plot_warping(query111, query112, path11)


distance, paths = dtw.warping_paths(query111, query112)
print(distance)


#%%

idx111 = price1.loc['index']
query111 = price1.iloc[4]
query113 = price1.iloc[6]

path11 = dtw.warping_path(query111, query113)
dtwvis.plot_warping(query111, query113, path11)


distance, paths = dtw.warping_paths(query111, query113)
print(distance)
print(paths)

#%%
idx111 = price1.loc['index']
query111 = price1.iloc[5]
query113 = price1.iloc[6]

path11 = dtw.warping_path(query111, query113)
dtwvis.plot_warping(query111, query113, path11)


distance, paths = dtw.warping_paths(query111, query113)
print(distance)


#%% 길이 다른 경우
import numpy as np

idx = np.linspace(0, 6.28, num = 100)
idx2 = np.linspace(0, 7.28, num = 200)

query = np.sin(idx) + np.random.uniform(size=100)/10.0
query2 = np.sin(idx2) + np.random.uniform(size=200)/10.0


distance, paths = dtw.warping_paths(query, query2)
print(distance)
print(paths)

import matplotlib.pyplot as plt
plt.plot(query)
plt.plot(query2)

paths = dtw.warping_path(query, query2)
dtwvis.plot_warping(query, query2, paths)


#%% 길이 같은 경우


#%%
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np
s1 = np.array([0., 0, 1, 2, 1, 0, 1, 0, 0, 2, 1, 0, 0])
s2 = np.array([0., 1, 2, 3, 1, 0, 0, 0, 2, 1, 0, 0, 0])
path = dtw.warping_path(s1, s2)
dtwvis.plot_warping(s1, s2, path)

distance, paths = dtw.warping_paths(s1, s2)
print(distance)

