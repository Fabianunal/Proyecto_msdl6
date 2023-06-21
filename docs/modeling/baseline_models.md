# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline. Se utilizaran varios modelos para extraer las caracteristicas de los datos, con el fin de no generar un sobre ajuste en el entrenamiento debido que no es conveniente entrenar un modelo con datos puros, es mejor tener las caracteristicas principales de los datos. 

## Descripción del modelo

Se utilizaran los tres tipos de extraccion de caracteristicas y se evaluaran dependiendo de su rendimiento a la hora de entrenar. La extraccion de carácteristicas se genera apartir de los A-scan generados por el radar GPR-UWB para esto se toma una parte de la señal donde se observa una variacion evidente del elemento enterrado, entonces cada radargrama tendra un tamaño de 100 x 500 frame donde los 100 datos son la sección donde está contenida la información mas relevante. 

# Extraccion de caracteristicas usando herramientas estadisticas. 
Esta extraccion se realizará sobre los 100 datos pero se hace un pequeño recorte a 60 dato con el fin de reduccir la dimensionalidad, luego se realizan la extraccion de las siguientes caracteristicas  mediante metodos estadisticos como el promedio, la desviación estandar, kurtosis y se alinean en un solo vector de 360 datos, dejando la matriz de cada elemento que antes era de 100 x 500 ahora en un solo vector. Para ver con más detalle esta extracción de caracteristicas  ver el archivo del repositorio que se encuentra en 

https://github.com/Fabianunal/Proyecto_msdl6/tree/master/scripts/preprocessing

# Extraccion de caracteristicas usando Matrix Pencil SEM
Esta extracción de caracteristicas no es muy común y es innovadora la cual se trata de extraer caracteristicas de una señal analizando las componentes en un plano complejo, osea extraer polos, los cual recontruyen la señal con una suma de senoides amortiguados, se extraen 16 polos de cada A-scan lo cual genera una matriz de 16 X 500 frame el cual hace una reduccion considerable de tamaño. al reconstruir la señal con estos polos nos da una exactitud del 99.7%. 
La extracción se encuentra en el siguiente codigo del repositorio. 

## Variables de entrada

LAs variables de entrada son las señales de los A-scan por 500 frames, lo cual constituye un radargrama. Estos A-scan inicialmente tiene un tamaño de 511 pero se reduccen a 100 datos. 

## Variable objetivo

La variable objetivo son los features estos deben ser un vector de menor tamaño. Por la reducción de dimensionalidad. 

## Evaluación del modelo
El modelo se evaluara mediante un RandomForestClassifier con datos balanceados y con una semilla de 2. 

### Métricas de evaluación

Las metricas de evaluación seran el accuracy que genere un modelo con los mismo hiperparametros, en este caso se utiliza el radomforest. 

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

## Referencias


