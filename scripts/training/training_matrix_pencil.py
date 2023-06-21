# -*- coding: utf-8 -*-
"""training_Matrix_pencil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vCYZYxVUXuFdoHLkKvdwquOV7tGEMG-d
"""

# Commented out IPython magic to ensure Python compatibility.
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
import re
import os
import h5py
import scipy.io
import urllib.request
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
# Actualizamos scikit-learn a la última versión
!pip install -U scikit-learn

# Importamos scikit-learn
import sklearn
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
# Librería de visualización interactiva - Plotly
!pip install -U plotly
import plotly
import plotly.express as px
import plotly.graph_objects as go



# Ignoramos las advertencias o warnings.
import warnings
warnings.simplefilter(action='ignore')

# Configuramos el formato por defecto de la
# librería de visualización Matplotlib.
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
mpl.rcParams['figure.dpi'] = 105
mpl.rcParams['figure.figsize'] = (9, 7)
sns.set_theme()

#Extrac data poles
with h5py.File("/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_real.h5", "r") as f:
    X_real = f['real'][:]

with h5py.File("/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_imag.h5", "r") as f:
    X_imag = f['imag'][:]

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/labels.h5', 'r') as f:
    y = f['labels'][:]

print(X_real.shape)
print(X_imag.shape)
print(y.shape)
X_real[0]
cero=np.sum(X_real==0)
print(cero)

# Every time than this code is run to reduce poles at half.
X_real = X_real[:,::2,:]
X_imag = X_imag[:,::2,:]


print(X_real.shape)
print(X_imag.shape)
print(y.shape)
X_imag[:,:,0]

X_t= np.concatenate((X_real, X_imag), axis=1)
print(X_t.shape)

mat= X_t.reshape(X_t.shape[1], -1)
mat_v = mat.ravel()
Xtrain = mat_v.reshape(X_t.shape[0], -1)
print("Tamaño de la nueva matriz:", Xtrain.shape)
Xtrain[10]

# value of the dimension4
# pca = PCA(n_components=600)
# X_transf = pca.fit_transform(Xtrain)

X_transf = Xtrain # descomentar para aplicar el PCA
#print(X_transf.shape)

# Data train 70%
X_train, X_test, y_train, y_test = train_test_split(X_transf, y, test_size=0.3, random_state=21)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Crear una instancia del modelo Random Forest
modelo_rf = RandomForestClassifier(class_weight='balanced', random_state=2)

# Train Model using data trains
modelo_rf.fit(X_train, y_train)

# Predit label for data test
y_pred_rf = modelo_rf.predict(X_test)

# Calcule the score the model Random Forest
precision_rf = accuracy_score(y_test, y_pred_rf)

# print la score
print("Precisión Random Forest:", precision_rf)