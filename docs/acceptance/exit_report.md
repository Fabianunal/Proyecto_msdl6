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
2) SEM-Matrix pencil: Se extrae caracteristicas usando Matrix pencil como metodo de expansion. Ete metodo se encarga de extraer los polos mas significativos de cada A-scan, con estos polos se construye un vector de caracteristicas para ser usado como los datos de entrenamiento y evaluación del modelo de ML random forest.

Despliegue: Se despliega el modelo con mayor desempeño con el uso de FastAPI.

- Evaluación del modelo final y comparación con el modelo base.


- Descripción de los resultados y su relevancia para el negocio.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
- Recomendaciones para futuros proyectos de machine learning.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
