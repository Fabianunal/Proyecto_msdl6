# -*- coding: utf-8 -*-
"""ML_feature_extraction_models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sEGof57R734EoNqh9UvHZ2fHK8mdlA22

#**Machine Learning - Statistical Approach/Feature Extraction**
---
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

# Time domain feature extraction methods - statistical approach
import scipy.stats as stats
from scipy.stats import skew
from scipy.stats import kurtosis

Lim=[10, 90]
mean = np.zeros((len(X), Lim[1]-Lim[0]))
std = np.zeros((len(X), Lim[1]-Lim[0]))
var = np.zeros((len(X), Lim[1]-Lim[0]))
rms = np.zeros((len(X), Lim[1]-Lim[0]))
abs_max = np.zeros((len(X), Lim[1]-Lim[0]))
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

Xdata=con
print(f' {Xdata.shape}')
print(f'{y.shape}')
abs_max.shape

"""## **Training Data - Full Data**
----

```
# This is formatted as code
```


"""

# Data train 70%
X_train, X_test, y_train, y_test = train_test_split(Xdata, y, test_size=0.3, random_state=2)
X_test.shape

"""## **Random Forest**
----

"""

from sklearn.ensemble import RandomForestClassifier
# Create an instance of RandomForestClassifier with balanced class weights
rf_classifier = RandomForestClassifier(n_estimators=150, class_weight='balanced')

# Fit the classifier to your training data
rf_classifier.fit(X_train, y_train)

# Make predictions on test data
y_pred = rf_classifier.predict(X_test)

# Evaluate the performance of the classifier
accuracy = rf_classifier.score(X_test, y_test)
print("Accuracy Random Forest:", accuracy)

# Only data test
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Predict the labels for the test data
y_pred = rf_classifier.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Create a heatmap of the confusion matrix
sns.heatmap(cm, annot=True,fmt=".2f", cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

from sklearn.metrics import classification_report, confusion_matrix

def evaluation(model, features_test, labels_test):
    y_pred = model.predict(features_test)
    report = classification_report(labels_test, y_pred)
    confusion = confusion_matrix(labels_test, y_pred)
    classes = np.unique(labels_test)
    fig, ax = plt.subplots()
    im = ax.imshow(confusion, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(confusion.shape[1]),
           yticks=np.arange(confusion.shape[0]),
           xticklabels=classes, yticklabels=classes,
           ylabel='True label',
           xlabel='Predicted label')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    for i in range(confusion.shape[0]):
        for j in range(confusion.shape[1]):
            ax.text(j, i, format(confusion[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if confusion[i, j] > confusion.max() / 2. else "black")
    fig.tight_layout()
    plt.show()
    return report

# look table with metrics of model:

report = evaluation(rf_classifier, Xdata, y)
print(report)

"""## **Sopport Vector Machine**
----
"""

from sklearn import svm
from sklearn.svm import NuSVC
from sklearn.metrics import accuracy_score

# Create an SVM classifier with balanced class weights
clf = svm.SVC(kernel="rbf", gamma='scale',degree=3,class_weight='balanced',random_state = 42)


# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Only data test
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Predict the labels for the test data
y_pred = clf.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Create a heatmap of the confusion matrix
sns.heatmap(cm, annot=True,fmt=".2f", cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

from sklearn.metrics import classification_report, confusion_matrix

def evaluation(model, features_test, labels_test):
    y_pred = model.predict(features_test)
    report = classification_report(labels_test, y_pred)
    confusion = confusion_matrix(labels_test, y_pred)
    classes = np.unique(labels_test)
    fig, ax = plt.subplots()
    im = ax.imshow(confusion, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(confusion.shape[1]),
           yticks=np.arange(confusion.shape[0]),
           xticklabels=classes, yticklabels=classes,
           ylabel='True label',
           xlabel='Predicted label')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    for i in range(confusion.shape[0]):
        for j in range(confusion.shape[1]):
            ax.text(j, i, format(confusion[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if confusion[i, j] > confusion.max() / 2. else "black")
    fig.tight_layout()
    plt.show()
    return report

report = evaluation(clf, Xdata, y)
print(report)

"""##**KNN**
-----
"""

from sklearn.neighbors import KNeighborsClassifier
# Create an instance of the KNeighborsClassifier with balanced weights
knn = KNeighborsClassifier(n_neighbors=6, weights='distance',algorithm='brute',metric='minkowski')

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.tree import DecisionTreeClassifier

# Create an instance of the DecisionTreeClassifier with balanced class weights
dt = DecisionTreeClassifier(class_weight='balanced')

# Train the classifier on the training data
dt.fit(X_train, y_train)

# Make predictions on the test data
y_pred = dt.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# Define the parameter grid to search over
param_grid = {
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': [None, 'balanced']
}

# Create an instance of the DecisionTreeClassifier
dt = DecisionTreeClassifier()

# Create an instance of GridSearchCV
grid_search = GridSearchCV(dt, param_grid, cv=5)

# Fit the GridSearchCV object to the data
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best Parameters:", best_params)
print("Best Score:", best_score)

## Futuros Analisis  Árbol de decisión por validación cruzada con Grid Search
from sklearn import metrics

# Módulos necesarios para realizar el ejercicio.
from sklearn import model_selection
from sklearn import tree

param_grid = {
    "max_depth": range(5, 60, 5),     # Profundidad máxima del árbol de decisión.
    "criterion": ["gini", "entropy"], # Criterio de partición del árbol.
  }
k=3

tree_clf = tree.DecisionTreeClassifier(random_state=0)
gsearch = model_selection.GridSearchCV(estimator=tree_clf, param_grid=param_grid, cv=k)
gsearch.fit(X_train, y_train)

best_model = gsearch.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
precision_macro = metrics.precision_score(y_test, y_pred, average='macro')
recall_macro = metrics.recall_score(y_test, y_pred, average='macro')
f1_macro = metrics.f1_score(y_test, y_pred, average='macro')

print(accuracy, precision_macro, recall_macro, f1_macro)