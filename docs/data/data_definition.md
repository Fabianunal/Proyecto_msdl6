# Definición de los datos
  
## Origen de los datos

- [ ] Especificar la fuente de los datos y la forma en que se obtuvieron.

En el marco de este proyecto se utiliza un dataset de medidas realizados por un sistema de penetración terrestre (GPR por sus siglas en inglés) ubicado en el campus de la Universidad Nacional de Colombia sede Bogotá. Las medidas tomadas por este sistema GPR corresponden a una serie de artefactos explosivos improvisados (IED por sus siglas en inglés) enterrados, junto con diversos elementos canónicos (cilindros) enterrados de diferentes materiales y dimensiones que serán etiquetados como Clutter. El objetivo de este proyecto es clasificar IEDs de Clutter (no IED) mediante el uso de técnicas de Machine Learning.

Las medidas se realizan desplazando el dispositivo GPR junto con los sensores (antenas) en un sistema de posicionamiento a una velocidad de 1 cm/s sobre el elemento canónico enterrado, obteniendo 500 IRF (Impulse Respond Function) en la zona medida. Esta quiere decir que cada elemento medido cuenta con 500 IRF o A-scan. El elemento bajo estudio se encuentra enterrado en la mitad exacta del recorrido realizado por el posicionador. Esto quiere decir, que el posicionador realiza un barrido de 50 cm y el centro geométrico del elemento se encuentra a 25 cm. Todos los elementos se encuentran a una profundidad de 5 cm.

Como es conocido la exploración con tegnologias GPR busca describir a traves de imagenes lo que se encuentra bajo la superficie en estudio. Por esta razón, es necesario tomar esos 500 IRF de cada elemento medido para formar una imagen llamada B-scan, que no es mas que la descripción de la firma hiperbolica producida por las ondas electromagneticas al hacer contacto con el elemento de interes que se encuentra bajo la superficie.

## Especificación de los scripts para la carga de datos

- [ ] Especificar los scripts utilizados para la carga de los datos.
En el script extract_data_train.ipynb se encuentra el codigo detallado para la carga de los datos:
https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/data_acquisition/extract_data_train.ipynb
En este script se extraen todos los A-scan de las medidas realizadas para los IEDs y para el clutter, creando dos tensores  *.h5 para importar los datos 'datas.h5' y 'labels.h5' donde se almacena la información A-scan del elemento medido y si es o no un IED.  

En el script main se extra la información de los tensores antes mencionados poara asi hacer la partición de entrenamiento y test para entrenar el modelo
https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/data_acquisition/main.py

## Referencias a rutas o bases de datos origen y destino

- [ ] Especificar las rutas o bases de datos de origen y destino para los datos.
El sistema GPR almacena las medidas realizadas en la siguiente dirección de Drive, el archivo almacenado por cada medida UWBdata.m contiene la información de la medida del objetivo bajo estudio (IED o Clutter) junto con metadatos porpios del sistema. La informacion de interes es extraida en el script extract_data_train.ipynb.
route ='/content/drive/Shareddrives/TII UNAL GPR/Data Set Measurements'


### Rutas de origen de datos

- [ ] Especificar la ubicación de los archivos de origen de los datos.
La información de interes extraida por extract_data_train.ipynb es almacenana en:
'/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/datas.h5
'/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/labels.h5'
Esta información tan solo contiene los A-scan de los objetivos bajo estudio (IED o CLutter)
- [ ] Especificar la estructura de los archivos de origen de los datos.
A-scan del elemento bajo estudio como 'datas.h5'
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/datas.h5', 'r') as f:
X = f['datas'][:]
Información del objetivo bajo estudio es o no IED
with h5py.File('/content/drive/Shareddrives/TII UNAL GPR/Machine Learning Models/Data Training/Raw Data/labels.h5', 'r') as f:
y = f['labels'][:]
- [ ] Describir los procedimientos de transformación y limpieza de los datos.
Cada medida contiene 500 A-scan y cada A-scan tiene 511 muestras formando un arreglo de (511,500), de los 511 muestras tan solo se seleccionan donde se encuentra el elemento bajo estudio, tomando tan solo 100 de estas muestras.




