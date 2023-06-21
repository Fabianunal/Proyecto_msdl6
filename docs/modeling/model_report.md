# Reporte del Modelo 

## Resumen Ejecutivo

El objetivo principal de este trabajo es desarrollar un radar de penetración terrestre de banda ultra ancha (UWB-GPR) basado en Inteligencia Artificial que se pueda programar, modificar y entrenar en diferentes escenarios o configuraciones experimentales con el propósito de operar en línea detectando y clasificando objetos enterrados a poca profundidad como minas terrestres e IEDs.

Este documento contiene los resultados del modelo final. Se utilizan metodos de extracción de caracteristicas en base a una aproximación estadistica, con el fin de no generar un sobre ajuste en el entrenamiento debido que no es conveniente entrenar un modelo con datos puros, es mejor tener las caracteristicas principales de los datos. Los parametros usados en el modelo principal son: media, desviación estandar, varianza, RMS, maximo absoluto y coeficiente de Skewness.

## Descripción del Problema

La detección de objetos enterrados a través de UWB-GPR es una técnica prometedora, puesto que permite extraer imágenes del suelo, donde es posible discriminar objetos, metálicos y no metálicos. El principio físico detrás de esta técnica es la extracción de información del medio (el suelo y los objetos plantados en él) a través de la comparación y procesado de dos señales: la emitida y la reflejada por el medio mismo [1-11]. El análisis y procesamiento de dicha información se ha hecho más prolífico y rápido, debido a la velocidad de procesamiento, accesibilidad y reducción de tamaño de los circuitos electrónicos digitales del momento.

Sin embargo, los sistemas GPR actuales presentan un importante inconveniente: la alta tasa de falsas alarmas producto del pobre nivel Señal/Clutter (SCR) presente en la operación del sistema [12, 13]. Esta condición de funcionamiento es la principal limitante en la utilización de las potencialidades de los sistemas GPR, y representa el mayor reto a la hora de diseñar e implementar un sistema de detección de objetos, utilizando esta técnica. Una promisoria alternativa para abordar el problema surge de la explotación del principio físico de máxima transmisión de potencia al suelo cuando éste es radiado en cierto ángulo, conocido como de Brewster, lo cual permitiría el aumento de la mencionada figura de mérito del sistema GPR: la SCR [14, 15]. Esto, bajo condiciones reales de suelos, como la no homogeneidad y la dispersión en el dominio de la frecuencia, por cuenta de la presencia de agua y de otros componentes que varían sus características eléctricas.

Sumado a esto, la resolución de las imágenes extraídas puede verse reducida por el bajo nivel de la figura de mérito SCR, independientemente de los algoritmos de reconocimiento de imagen. Una alternativa es el uso de algoritmos IA cognitivos que evalúen de forma fiable la calidad de la imagen, y compense los parámetros de hardware y software del sistema de imágenes, con el fin de mejorar la SCR. Así, las figuras de mérito apropiadas deben ser establecidas, tales que capturen las características de la imagen central, como la nitidez y el contraste. Los primeros experimentos han demostrado que la detección de elementos enterrados en el suelo puede facilitarse utilizando una distribución adecuada de los gradientes de la imagen SAR [16]. Otras posibles cantidades son la forma y anchura de la función de dispersión puntual de blancos de baja sección radar (RCS).

En ese sentido, este trabajo tiene como objetivo integrar el entrenamiento y funcionamiento de un algoritmo de ML y el sistema GPR. Para lograrlo, es necesario abordar las siguientes preguntas de investigación: ¿Cuál es la relación del ángulo óptimo de incidencia (ángulo de Brewster) con el comportamiento eléctrico de suelos no homogéneos, laminados y de alto contenido de agua (relación Señal/Clutter)? y ¿Como el uso algoritmos de Machine Learning  pueden aumentar la precisión y versatilidad en el reconocimiento de patrones, detección y clasificación de objetos a partir de A-scan?

## Descripción del Modelo

La extracción de caracteristicas en el dominio del tiempo planteadas para este modelo se realizan mediante el uso de parametras estadisticos; media, desviación estandar, varianza, RMS, maximo absoluto y coeficiente de Skewness. Esta extraccion de carácteristicas se genera apartir de los A-scan generados por el radar GPR-UWB para esto se toma una parte de la señal donde se observa una variacion evidente del elemento enterrado, entonces cada radargrama tendra un tamaño de 100 x 500 frame donde los 100 datos son la sección donde está contenida la información mas relevante.

Esta extraccion se realizará sobre los 100 datos pero se hace un pequeño recorte a 80 dato con el fin de reduccir la dimensionalidad, luego se realizan la extraccion de las siguientes caracteristicas mediante metodos estadisticos como el promedio, la desviación estandar, kurtosis y se alinean en un solo vector de 480 datos, dejando la matriz de cada elemento que antes era de 100 x 500 ahora en un solo vector. Para ver con más detalle esta extracción de caracteristicas ver el archivo del repositorio que se encuentra en

https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/preprocessing/statistical_approach_feature_extraction.py

Partiendo de las caracteristicas extraidas se dividen los datos en 70% y 30% para entrenamiento y prueba respectivamente, evaluando asi el modelo RandomForestClassifier con datos balanceados y con una semilla de 2.

## Evaluación del Modelo

Las metricas de evaluación seran el accuracy que genere un modelo con los mismo hiperparametros, en este caso se utiliza el radomforest. En el script utilizado para el entrenamiento de este enfoque estadistico:
Script de training usando statistical approach https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/preprocessing/ml_feature_extraction_models.py.

De los resultados mas relevantes se tiene una matriz de confusión:
https://github.com/Fabianunal/Proyecto_msdl6/blob/master/docs/modeling/MC_MLDS.PNG
en la que se puede apreciar que el modelo considera 3 IEDs como no artefactos explosivos y 17 no IEDs como artefactos explosivos. En el promer caso es de alto riesgo esa predicción ya que la vida del desminador se encuentra en riesgo.

| Caracteristica | tamaño Tensor |   Accuracy |
|------|---------|-------|
| Features usando estadistica | 1901 x 480 |  0.9649 |

## Conclusiones y Recomendaciones

El modelo es un planteamiento sencillo de extraccion de caracteristicas para un sistema GPR que produce IRFs de gran complejidad. Al evaluar cada parametro por separado el rendimiento del modelo es muy pobre pero al concatenar todos los parametros mencionados con anterioridad en este documento el modelo aumenta su rendimiento de forma considerable, el proposito a futuro es considerar nuevos parametros que lleven el modelo a elevar aun mas su rendimiento.

Puntos Fuertes:
Modelo sencillo.
Facil de implementar.
Alto accuracy.

Puntos debiles:
Suceptible al ruido.
Cambio del comportamiento de A-scan por el uso de otra antena.

Debilidades:
Es posible que no sea un modelo resilente al encontrar datos A-scan con ruido EM, velocidades diferentes de muestreo cambiando el numero de frames medidos por el sistema GPR. 



## Referencias

[1] C. Baer, J. Barowski, J. Jebramcik, S. Gutierrez, F. Vega, I. Rolfes, “Ground Penetrating Synthetic Aperture Radar Imaging Providing Soil Permittivity Estimation” in Proceedings IEEE MTT-SInternational Microwave Symposium 2017, Honolulu, Hawaii, USA

[2] Gutierrez S., Just T., Sachs J., Baer C., Vega F. “Field Deployable System for the Measurement of Complex Permittivity of Improvised Explosives and Lossy Dielectric Materials” in IEEE Sensors Journal, in revision.

[3] D. Martinez, S. Gutierrez, S.Rodriguez, F. Vega, R. Bustamante, J. Sachs, C. Baer, “UWB backscattering characterization of improvised explosive devices”, European Electromagnetic Symposium 2016, London, UK

[4] S. A. Gutierrez, E. Neira, J. J. Pantoja, and F. Vega, ‘The effect of ANFO on the Complex Resonance Frequencies of an IED’, in Asia Electromagnetic Conference. ASIAEM, 2015

[5] S. A. Guitierrez ‘Application of Time-Frequency Transformations in Polarimetric Ultra-Wideband MIMO-GPR signals for Detection of Colombian Improvised Explosive Devices’. Universidd Nacional de Colombia, Bogota. Facultad de Ingenieria Departamento de Ingenieria Electrica y Electronica. 2019.
[6] P. M. Barone and L. Desibio, "Landscape archaeology of southern Umbria (Italy) using the GPR technique,"8th Int. Workshop on Advanced Ground Penetrating Radar (IWAGPR), Florence, 2015, pp. 1-4.

[7] F. Jonard, L. Weihermuller, K. Z. Jadoon, M. Schwank, H. Vereecken and S. Lambot, "Mapping Field-Scale Soil Moisture With L-Band Radiometer and Ground-Penetrating Radar Over Bare Soil," in IEEE Transactions on Geoscience and Remote Sensing, vol. 49, no. 8, pp. 2863- 2875, Aug. 2011.

[8] K. C. Ho, L. M. Collins, L. G. Huettel and P. D. Gader, "Discrimination mode processing for EMI and GPR sensors for hand-held land mine detection," in IEEE Transactions on Geoscience and Remote Sensing, vol. 42, no. 1, pp. 249-263, Jan. 2004.

[9] F. Fruehauf, A. Heilig, M. Schneebeli, W. Fellin and O. Scherzer, "Experiments and Algorithms to Detect Snow Avalanche Victims Using Airborne Ground-Penetrating Radar," in IEEE Transactions on Geoscience and Remote Sensing, vol. 47, no. 7, pp. 2240-2251, July 2009.

[10] J. Sachs, "M-sequence radar". In Ground Penetrating Radar, 2nd edition, D. J. Daniels, Ground Penetrating Radar. IET Radar, Sonar, Navigation and Avionics Series 15, pp. 225-237, 2004.

[11] J. Sachs, Handbook of Ultra-Wideband Short-Range Sensing - Theory, Sensors, Applications. Berlin: Wiley-VCH, 2012.

[12] Brewster D., “On the Laws Which Regulate the Polarisation of Light by Reflexion from Transparent Bodies”, Philosophical Transactions of the Royal Society of London, vol. 105, pp. 125- 159, 1815.

[13] Thomson L., Osinski G. R., y Pollard W., “Application of the Brewster angle to quantify the dielectric properties of ground ice formations”, Journal of Applied Geophysics, vol. 99, pp. 12-17, dic. 2013.

[14] Ohman G., “The pseudo-Brewster angle”, IEEE Transactions on Antennas and Propagation, vol. 25, n.o 6, pp. 903-904, nov. 1977.

[15] K. Ouchi, C. S. Yang, "Direct evidence and implications of Brewster's angle damping observed by synthetic aperture radar images," 2017 IEEE International Geoscience and Remote Sensing Symposium (IGARSS), Fort Worth, TX, 2017, pp. 5338-5341.

[16] T. G. Savelyev, L. van Kempen, H. Sahli, J. Sachs and M. Sato, "Investigation of Time–Frequency Features for GPR Landmine Discrimination," in IEEE Transactions on Geoscience and Remote Sensing, vol. 45, no. 1, pp. 118-129, Jan. 2007.

