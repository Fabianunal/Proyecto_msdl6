# -*- coding: utf-8 -*-
"""Statistical Approach_Feature Extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n2mSdP50f3EVfbyuDuNhd97a83ELIQfQ

#**Machine Learning - Statistical Approach/Feature Extraction**
--------------------
"""

#Install librarys
from google.colab import drive
drive.mount('/content/drive')
import numpy as np
import pandas as pd
import re
import os
import h5py
import scipy.io
import matplotlib.pyplot as plt
import urllib.request
# Upgrade scikit-learn the final version
!pip install -U scikit-learn
# Import scikit-learn
import sklearn
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import matplotlib as mpl
import seaborn as sns
# Librería de visualización interactiva - Plotly
!pip install -U plotly
import plotly
import plotly.express as px
import plotly.graph_objects as go

# Commented out IPython magic to ensure Python compatibility.
# Import the warnings module to manage warning messages
import warnings
# Set the filter action to ignore warnings
warnings.simplefilter(action='ignore')
# Enable inline plotting in Jupyter Notebook or JupyterLab
# %matplotlib inline
# Set the figure format to 'retina' for high-resolution figures
# %config InlineBackend.figure_format = 'retina'
# Set the DPI (dots per inch) of the figures
mpl.rcParams['figure.dpi'] = 105
# Set the default size of the figures
mpl.rcParams['figure.figsize'] = (9, 7)
# Set the default theme for Seaborn
sns.set_theme()

"""## **GPR-Raw Data to Tensor Data**
----
"""

# Read the .h5 file-pandas DataFrame

# Load data from the first HDF5 file
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/datas.h5', 'r') as f:
    X = f['datas'][:]

# Load data from the second HDF5 file
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/labels.h5', 'r') as f:
    y = f['labels'][:]

"""Time domain feature extraction methods - statistical approach"""

# Time domain feature extraction methods - statistical approach
import scipy.stats as stats
from scipy.stats import skew
from scipy.stats import kurtosis

Lim=[10, 90]
# Mean
mean = np.zeros((len(X), Lim[1]-Lim[0]))
# Standard Deviation
std = np.zeros((len(X), Lim[1]-Lim[0]))
# Variance
var = np.zeros((len(X), Lim[1]-Lim[0]))
# RMS
rms = np.zeros((len(X), Lim[1]-Lim[0]))
# Absolute Maximum
abs_max = np.zeros((len(X), Lim[1]-Lim[0]))
# Coefficient of Skewness
skewness = np.zeros((len(X), Lim[1]-Lim[0]))

con = np.zeros((len(X), (Lim[1]-Lim[0])*6))

for x in range(len(X)):
# add the vectors by column
  rw_mean = np.mean(X[x].T, axis=0)
  rw_std = np.std(X[x].T, axis=0)
  rw_var = np.var(X[x].T, axis=0)
  rw_rms = np.sqrt(np.mean(np.square(X[x].T), axis=0))
  rw_abs_max = np.max(np.abs(X[x].T), axis=0)
  rw_skewness = skew(X[x].T, axis=0)


  mean[x]=rw_mean[Lim[0]:Lim[1]]
  std[x]=rw_std[Lim[0]:Lim[1]]
  var[x]=rw_var[Lim[0]:Lim[1]]
  rms[x]=rw_rms[Lim[0]:Lim[1]]
  abs_max[x]=rw_abs_max[Lim[0]:Lim[1]]
  skewness[x]=rw_skewness[Lim[0]:Lim[1]]

  con[x]=np.concatenate([mean[x], std[x], var[x],rms[x],abs_max[x],skewness[x]])

Xdata=std
print(f' {Xdata.shape}')
print(f'{y.shape}')
abs_max.shape

"""## **Graphics**
------

"""

x = np.arange(0,Lim[1]-Lim[0],1)
fig, ax = plt.subplots(nrows=7, ncols=1, figsize=(8,20))

ax[0].plot(x,X[0,10:90])#label="Frame" )
ax[0].set_xlabel('Samples')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Dataframe - 500 frames')
ax[0].legend()
ax[0].grid()

ax[1].plot(x, mean.T)
ax[1].set_xlabel('Samples')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Mean - Data training')
ax[1].legend()
ax[1].grid()

ax[2].plot(x,std.T)
ax[2].set_xlabel('Samples')
ax[2].set_ylabel('Amplitude')
ax[2].set_title('Standard Deviation - Data Training')
ax[2].legend()
ax[2].grid()

ax[3].plot(x,var.T)
ax[3].set_xlabel('Samples')
ax[3].set_ylabel('Amplitude')
ax[3].set_title('Variance - Data Training')
ax[3].legend()
ax[3].grid()

ax[4].plot(x,rms.T)
ax[4].set_xlabel('Samples')
ax[4].set_ylabel('Amplitude')
ax[4].set_title('RMS - Data Training')
ax[4].legend()
ax[4].grid()

ax[5].plot(x,abs_max.T)
ax[5].set_xlabel('Samples')
ax[5].set_ylabel('Amplitude')
ax[5].set_title('Absulute maximum - Data Training')
ax[5].legend()
ax[5].grid()

ax[6].plot(x,skewness.T)
ax[6].set_xlabel('Samples')
ax[6].set_ylabel('Amplitude')
ax[6].set_title('Coefficient of Skewness - Data Training')
ax[6].legend()
ax[6].grid()


plt.subplots_adjust(hspace=0.5)
plt.show()