# -*- coding: utf-8 -*-
"""extract_poles_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NA4jy3M_OYomIpe-xz2kOHm6rBKq30JV

# Librerias
"""

# Librerias
from google.colab import drive
drive.mount('/content/drive')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import h5py

"""## Function Matrix Pencil"""

#other Function

def MatrixPencil(f, t, M):
    ft = f
    #print(ft.shape)
    N = len(ft)
    #print(N)

    L = int(N / 2)
    dt = t[1] - t[0]

    # Generación de matriz Y
    Y = Hankel(ft, L, N)

    # Descomposición en valores singulares de matriz Y
    U, S, V = svd(Y)
    #print(f'Primer SVD = {S.shape}')

    Vp = V[:, :M]
    #print(f'Vp = {Vp.shape}')
    hh, h = Vp.shape
    V2 = Vp[1:hh, :]

    V1 = Vp[:hh - 1, :]

    G = Gamma(V1, V2, M)
    se = np.log(G)
    Si = se / dt

    # Reconstrucción de señal
    Ri = Reb(Si, M, N, ft, t)
    tiempo = time.time()

    # Cálculo de coeficiente de correlación
    ftr = np.zeros(N)
    for i in range(M):
        ftr += (Ri[i] * np.exp(Si[i] * t)).real

    ft1 = np.transpose(ft)
    dif = (ft1).real - ftr

    Bbar = np.mean(ft1.real)
    SStot = np.sum((ft1.real - Bbar) ** 2)
    SSres = np.sum((ftr.real - ft1.real) ** 2)
    R2 = 1 - SSres / SStot

    return Si, dif, ftr, tiempo, R2, Ri


def Hankel(ft, L, N):
    Y = np.zeros((L, N - L + 1))
    j = 0
    while j < (N - L):
        i = 0
        while i < (L + 1):
            if j == 0:
                Y[j, i] = ft[i]
            else:
                Y[j, i] = ft[i + j]
            i += 1
        j += 1

    #print(len(Y))
    return Y



def Gamma(V1, V2, M):

    #print(f'V1 = {V1.shape}')
    Uv, Sv, Vv = svd(V1.T)
    #print(Sv.shape)
    (r, w) = Sv.shape
    Svp = np.zeros((w, r))
    for j in range(r):
        for i in range(w):
            if j == i:
                Svp[i, j] = 1 / Sv[j, i]
            else:
                Svp[i, j] = Sv[j, i]

    V1c = V1.T
    V2c = V2.T
    #print(Vv.shape, Svp.shape, Uv.T.shape, V2c.shape)
    psi = Vv @ Svp @ Uv.T @ V2c
    #print(psi.shape)

    Ga = np.linalg.eigvals(psi)
    #print(len(Ga))

    Ga = np.linalg.eigvals(psi)
    Gamma = Ga[:M]

    #print(Gamma)
    return Gamma
    # Gamma = np.zeros(M)

    # for i in range(M):
    #     Gamma[i] = Ga[i]
    # return Gamma
    #print('Alcanza a llegar aqui')

def Reb(Si, M, N, ft, t):
    Van = np.zeros((N, M), dtype=complex)
    for n in range(N):
        for m in range(M):
            Van[n, m] = np.exp(Si[m] * t[n])

    Ri = np.linalg.lstsq(Van, ft, rcond=None)[0]
    Ri = np.transpose(Ri)

    return Ri

def svd(Y):
    U, sdiag, VH = np.linalg.svd(Y)

    S = np.zeros((len(U), len(VH)))
    np.fill_diagonal(S, sdiag)
    V = VH.T.conj()

    return U,S,V

"""# Extra Data

"""

#Extact Data Tensor
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/datas.h5', 'r') as f:
    X = f['datas'][:]

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/labels.h5', 'r') as f:
    y = f['labels'][:]

"""## Analisis de un radargrama"""

## Arreglo de datos
Lim=[0, 100]
rws = X[0].T # signal acotade
print(rws.shape)

#Grafics of radargrama
x = np.arange(0,Lim[1]-Lim[0],1)
plt.plot(x,rws.T)#label="Frame" )
plt.xlabel('IFRs')
plt.ylabel('Time [ns]')
plt.title('One DataFrame, there are 500 frames')
plt.legend()
plt.grid()

from numpy.lib.shape_base import row_stack
x = np.arange(0,Lim[1]-Lim[0],1)
M=16
pole=np.zeros((rws.shape[0],M*2))
R=np.zeros((rws.shape[0],M))
I=np.zeros((rws.shape[0],M))

print(pole.shape)

j=0
for  rw in rws:
  Si = MatrixPencil(rw, x, M)[0]
  R[j]=Si.real
  I[j]=Si.imag
  z=np.concatenate((Si.real, Si.imag))
  pole[j]=z
  j+=1

#print(pole.shape)

# print(pole[0])

# Grafics full radargram with poles, the poles is moving.

M=16
for c in range(M):
    plt.plot(R, I, 'o')

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.show()

"""## Genering Tensor of Poles of DataMeasures


"""

X.shape

## Arreglo de datos
Lim=[0, 100]
M=16
x = np.arange(0,Lim[1]-Lim[0],1)
X_real=np.zeros((X.shape[0], M, X.shape[2]))
X_imag=np.zeros((X.shape[0], M, X.shape[2]))
i=0;
for k in X:
  rws = k.T # signal aprint(X_real.shape)cotade
  pole=np.zeros((rws.shape[0],M*2))
  R=np.zeros((rws.shape[0],M))
  I=np.zeros((rws.shape[0],M))
  j=0
  for  rw in rws:
    Si = MatrixPencil(rw, x, M)[0]
    R[j]=Si.real
    I[j]=Si.imag
    z=np.concatenate((Si.real, Si.imag))
    pole[j]=z
    j+=1

  X_real[i]=R.T
  X_imag[i]=I.T
  i+=1

print(X_real.shape)

archivo_r = h5py.File("/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_real.h5", "w")
datos = archivo_r.create_dataset("real", data=X_real)
archivo_r.close()
archivo_i = h5py.File("/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_imag.h5", "w")
datos = archivo_i.create_dataset("imag", data=X_imag)
# Cerrar el archivo HDF5
archivo_i.close()

print(X_real[0])
print(X_imag.shape)

print(X_real[0][0])
print(X_imag.shape)

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/labels.h5', 'w') as f:
    f.create_dataset('labels', data=y)

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_real.h5', 'r') as f:
    real = f['real'][:]

with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/tmp/data/poles_train/data_imag.h5', 'r') as f:
    imag = f['imag'][:]

print(real[0])
print(imag.shape)