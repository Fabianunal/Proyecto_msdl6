# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline. Se utilizaran varios modelos para extraer las caracteristicas de los datos, con el fin de no generar un sobre ajuste en el entrenamiento debido que no es conveniente entrenar un modelo con datos puros, es mejor tener las caracteristicas principales de los datos. 

## Descripción del modelo

Se utilizaran los tres tipos de extraccion de caracteristicas y se evaluaran dependiendo de su rendimiento a la hora de entrenar. La extraccion de carácteristicas se genera apartir de los A-scan generados por el radar GPR-UWB para esto se toma una parte de la señal donde se observa una variacion evidente del elemento enterrado, entonces cada radargrama tendra un tamaño de 100 x 500 frame donde los 100 datos son la sección donde está contenida la información mas relevante. 

### Extraccion de caracteristicas usando herramientas estadisticas. 
Esta extraccion se realizará sobre los 100 datos pero se hace un pequeño recorte a 60 dato con el fin de reduccir la dimensionalidad, luego se realizan la extraccion de las siguientes caracteristicas  mediante metodos estadisticos como el promedio, la desviación estandar, kurtosis y se alinean en un solo vector de 360 datos, dejando la matriz de cada elemento que antes era de 100 x 500 ahora en un solo vector. Para ver con más detalle esta extracción de caracteristicas  ver el archivo del repositorio que se encuentra en 

https://github.com/Fabianunal/Proyecto_msdl6/tree/master/scripts/preprocessing

### Extraccion de caracteristicas usando Matrix Pencil SEM
Esta extracción de caracteristicas no es muy común y es innovadora la cual se trata de extraer caracteristicas de una señal analizando las componentes en un plano complejo, osea extraer polos, los cual recontruyen la señal con una suma de senoides amortiguados, se extraen 16 polos de cada A-scan lo cual genera una matriz de 16 X 500 frame el cual hace una reduccion considerable de tamaño. al reconstruir la señal con estos polos nos da una exactitud del 99.7%. 
La extracción se encuentra en el siguiente codigo del repositorio donde explica de forma mas detalla este metodo de extracción de caracteristias. 

https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/preprocessing/extract_poles_data.py 


## Variables de entrada

LAs variables de entrada son las señales de los A-scan por 500 frames, lo cual constituye un radargrama. Estos A-scan inicialmente tiene un tamaño de 511 pero se reduccen a 100 datos. se tienen 1901 datos el cual contituyr un tensor de entrada de 1901 X 100 X 500 donde 1455 son IEDs y 446 son Clutter, hasta el momento el sistema nos esta muy balanceado por esa razón se usa Random Forest ya que este modelo permite balancear los datos. 
 
## Variable objetivo

La variable objetivo son los features estos deben ser un vector de menor tamaño. Por la reducción de dimensionalidad. 

## Evaluación del modelo
Se deviden los datos en 70% y 30% para entrenamiento y para prueba respectivamente. 

El modelo se evaluara mediante un RandomForestClassifier con datos balanceados y con una semilla de 2. 

### Métricas de evaluación

Las metricas de evaluación seran el accuracy que genere un modelo con los mismo hiperparametros, en este caso se utiliza el radomforest. 

### Resultados de evaluación
Script de trainig usando matrix pencil
https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/training/training_matrix_pencil.py

| Caracteristica | tamaño Tensor |   Accuracy |
|------|---------|-------|
| Features usando estadistica | 1901 x 360| |
| Features usando Matrix Pencil | 1901 x 8000 |  0.9071 |


## Análisis de los resultados
### Usando herramientas estadisticas
Usando esta herramienta el vector de entranamiento final es muy corto a compracion del inicial, y permite no siempre tener los 500 frames, el cual tiene una gran ventaja en mediciones en campo donde no se logren los 500 data frames. Además las extracciones son muy rapidas para todo el data Set. 

### Usando Matrix Pencil SEM
Es una herramienta innovadora para extraer caracteristicas, una desventaja es que esta limitada a los 500 frames y el modelo se entrena teniendo encuenta la cantifdad de frame, y si no tiene esa cantidad de frames, el modelo no se podria aplicar, ademas extraer las caracteristicas de cada A-scan es muy demorado, para este data set se demora unas 4 horas aproximadamente. El accuracy no es muy alto. 

## Conclusiones

El metodo de Matrix pencil es innovador pero es muy practico por el coste computacional y por los resultados finales, cabe recalcar que se puede hacer mejores optimizaciones al modelo, pero frente a los modelos estadisticos inicialmente es inferior. 

La extracción por metodos estadisticos es muy bueno, y realmente tiene muy bueno resultados a pesar de su simplicidad. 

## Referencias

E. F. Ruiz, D. Chaparro-Arce, J. J. Pantoja, F. Vega, C. Kasmi and F. Al Yafei, "Ground Penetrating Radar Radargram Filter using Singularity Expansion Method," 2020 International Applied Computational Electromagnetics Society Symposium (ACES), Monterey, CA, USA, 2020, pp. 1-2, doi: 10.23919/ACES49320.2020.9196132



