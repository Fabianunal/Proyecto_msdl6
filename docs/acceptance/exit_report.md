# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

En el marco de este proyecto se utiliza un dataset de medidas realizados por un sistema de penetración terrestre (GPR por sus siglas en inglés) ubicado en el campus de la Universidad Nacional de Colombia sede Bogotá. Las medidas tomadas por este sistema GPR corresponden a una serie de artefactos explosivos improvisados (IED por sus siglas en inglés) enterrados, junto con diversos elementos canónicos (cilindros) enterrados de diferentes materiales y dimensiones que serán etiquetados como Clutter. El objetivo de este proyecto es clasificar IEDs de Clutter (no IED) mediante el uso de técnicas de Machine Learning.

Las medidas se realizan desplazando el dispositivo GPR junto con los sensores (antenas) en un sistema de posicionamiento a una velocidad de 1 cm/s sobre el elemento canónico enterrado, obteniendo 500 IRF (Impulse Respond Function) en la zona medida. Esta quiere decir que cada elemento medido cuenta con 500 IRF o A-scan. El elemento bajo estudio se encuentra enterrado en la mitad exacta del recorrido realizado por el posicionador. Esto quiere decir, que el posicionador realiza un barrido de 50 cm y el centro geométrico del elemento se encuentra a 25 cm. Todos los elementos se encuentran a una profundidad de 5 cm.

omo es conocido la exploración con tegnologias GPR busca describir a traves de imagenes lo que se encuentra bajo la superficie en estudio. Por esta razón, es necesario tomar esos 500 IRF de cada elemento medido para formar una imagen llamada B-scan, que no es mas que la descripción de la firma hiperbolica producida por las ondas electromagneticas al hacer contacto con el elemento de interes que se encuentra bajo la superficie.


## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
  
Entedimiento del negocio: En esta etapa se realiza un estudio del estado del arte con el proposito de comprender todos los fenomenos EM que se presentan al realizar medidas con un sistema GPR. Ademas, las diferentes tecnicas de adquisición de datos GPR en busca de obtener imagenes mas claras y con menor clutter.

Preprocesamiento y analisis exploratorio de los datos: En esta etapa se decide tomar los datos crudos obtenidos por el sistema GPR, pero para poder trabajar con estos datos se requiere una extracción de la información de interes de un archivo *mat, el cual cuenta con mayor informacion denominada metadata. La extracción de las medidas se realiza mediante un codigo desarrollado en python. Posterior a la extracción, se hace un analisis exploratorio de los datos mediante la construcción de los B-scan al apilar los 500 A-scan que cosntruyen la imagen de radar. En este proceso se determina la calidad de los datos.

Modelamiento y extracción de caracteristicas: En esta etapa se recurre a dos metodologias diferentes para realizar la extracción de caracteristicas:

1) Aproximación estadistica: Se realiza las extración de caracteristicas de cada A-scan mediante el uso de parametros estadisticos con el cual se construye un vector de caracteristicas para ser usado como los datos entrenamiento y evaluación del modelo de ML random forest.
2) SEM-Matrix pencil: Se extrae caracteristicas usando Matrix pencil como metodo de expansion. Este metodo se encarga de extraer los polos mas significativos de cada A-scan, con estos polos se construye un vector de caracteristicas para ser usado como los datos de entrenamiento y evaluación del modelo de ML random forest.

Despliegue: Se despliega el modelo con mayor desempeño con el uso de FastAPI.

- Evaluación del modelo final y comparación con el modelo base.

| Caracteristica | tamaño Tensor |   Accuracy |
|------|---------|-------|
| Features usando estadistica | 1901 x 480 |  0.9649 |
| Features usando Matrix Pencil | 1901 x 8000 |  0.9071 |

- Descripción de los resultados y su relevancia para el negocio.

El modelo estadistico para la extracción de caracteristicas tienen una menor complejidad tanto computacional como matematica y alcanza un accuracy mas elevado en comparación al metodo de SEM-MPM el cual requiere un eleveado costo computacional. Al tener un modelo con un despligue computacional inferior permite una implementación mas sencilla en diversas plataformas como los sitemas embebidos siendo de gran relevancia en el momento evaluar el modelo en sistemas GPR portables con el proposito de realizar una detección y clasificación en tiempo real de una mina antipersonal o IED, lo que representa la integridad del equipo humano de desminado. 

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.

1) La antena y configuración indicada para realizar las medidas en campo, ya que de estas depende la calidad de las señales emitidas por el GPR.
2) El evaluar modelos de ML usando datos crudos o procesados.
3) La implementación de diferentes modelos de ML.

- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.

1) Es importante tener un conjunto de datos sin errores producidos en este caso por ruido EM.
2) Tener en cuenta los datos es diferentes estados (crudos y procesados).
3) La prueba de difeentes modelos de ML con los diferentes estaods de los datos es de vital importancia ya que se determina el efecto de un preporcesamiento sobre los datos.
   
- Recomendaciones para futuros proyectos de machine learning.

1) Un dataset mas extenso.
2) Mayor cantidad de pruebas teneido encuenta la modificación de los hiperparametros.
   
## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.

  El desarrollo a cabalidad de una proyecto de esta magnitud se representa en la vida de los desminadores que se encuentran en campo.
  
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

 1) Lograr incrementar el numero de medidas para alimentar el modelo.
 2) Construir un sistema GPR portable y autonomo que realice evaluaciones de modelos ML/DL en tiempo real para la detección de minas terrestres antipersonas.
  

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.

  Se logro obtener un accuracy de 96% usando el modelo de extracción de caracterisiticas y entrenado un modelo RF.
  El desarrollo de un modelo con un accuracy alto representa la integridad del equipo desminador.
  
- Conclusiones finales y recomendaciones para futuros proyectos.

   El empleo de técnicas de procesamiento de señales, incluidas las funciones de transferencia lineal, el filtrado por reflexión y la sustracción del fondo, ha demostrado su eficacia para reducir las interferencias y mejorar la detección de minas terrestres en los datos de GPR. Estas técnicas abordan fenómenos electromagnéticos complejos y pretenden mejorar la fiabilidad y precisión de la detección de minas terrestres mediante GPR.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.

  Al equipo de medidas, asesores cientificos.
  
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.

  Technology Innovation Institute - UAE
