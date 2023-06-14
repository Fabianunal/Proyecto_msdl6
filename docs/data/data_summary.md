# Reporte de Datos

Explicacion de los datos de entrenamiento. 

https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/data_acquisition/extract_data_train.ipynb
## Resumen general de los datos

El entrenamiento de datos tiene 1901 mediciones, estos son dos tipos, el primer tipo es un radargrama de ladmain, el segundo dato es Clutter. Cada dato es un tensor de 511 x 500, en este caso tomamos solo 100 muestras del 511, La matriz de entrenamiento tiene una dimensión de 100 X 500. 

## Resumen de calidad de los datos

La calidad de los datos, presenta una SNR bajo, lo cual significa que tiene poco ruido la señal. Son señales muy trabajables inicialmente se realiza el trabajo sobre las señales sin procesar, las señales puras montadas sobre la antena que emite y recibe la señal. 

## Variable objetivo

La variable objetivo son los A-scan, lo cual son las IRF que genera el radar y contiene la informacion del objeto que se encuentra bajo tierra , debido a las señales retrodispersadas o de Scattering. Para ver mejor el tipo de pulso de las señales ver en el repositorio el sisguiente .ipynb

https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/data_acquisition/extract_data_train.ipynb

## Variables individuales

A las variables se le puede realizar treansformaciones, con el fin de extraer caracteristicas, se trabajan dos formas de extraccion de caracteristicas la primera es por metodos estadisticos, la segunda usando MAtrixpencil o SEM el cual expresa la señales como una suma de sinoides amortiguados. Estos se llaman los polos de la señal, y las Tercera es por metodos como PCA.  

## Ranking de variables

Las variables tienen los mismo pesos. en el procesamiento todas tiene el mismo nivel de importancia. 

## Relación entre variables explicativas y variable objetivo

Cada B-scan es la union de los A-scan estas contiene pequeñas diferencias que se pueden observar cuando se le aplica desviaciones estandar y promedio y se comparan entre B-scan. 

