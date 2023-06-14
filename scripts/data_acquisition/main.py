# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Hew4YXUainR-zImGQKDyhpBHnK3wJEG
"""

# %--------------------------------------------------------------------------
# %                                 RADAR B-SCAN
# %--------------------------------------------------------------------------
#
#In this Code we do differents probe of train of stup real of meansure.

# %--------------------------------------------------------------------------


from google.colab import drive
drive.mount('/content/drive')
import numpy as np
import pandas as pd
import os
import h5py


#Extract data
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/datas.h5', 'r') as f:
    X = f['datas'][:]

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/labels.h5', 'r') as f:
    y = f['labels'][:]

ladmine= np.sum(y==1)
clutter = np.sum(y==0)
print(f'Amount of ladmines are {ladmine}')
print(f'Amount of Clutters are {clutter}')