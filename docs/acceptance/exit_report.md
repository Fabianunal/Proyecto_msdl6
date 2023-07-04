# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

En el marco de este proyecto se utiliza un dataset de medidas realizados por un sistema de penetración terrestre (GPR por sus siglas en inglés) ubicado en el campus de la Universidad Nacional de Colombia sede Bogotá. Las medidas tomadas por este sistema GPR corresponden a una serie de artefactos explosivos improvisados (IED por sus siglas en inglés) enterrados, junto con diversos elementos canónicos (cilindros) enterrados de diferentes materiales y dimensiones que serán etiquetados como Clutter. El objetivo de este proyecto es clasificar IEDs de Clutter (no IED) mediante el uso de técnicas de Machine Learning.

Las medidas se realizan desplazando el dispositivo GPR junto con los sensores (antenas) en un sistema de posicionamiento a una velocidad de 1 cm/s sobre el elemento canónico enterrado, obteniendo 500 IRF (Impulse Respond Function) en la zona medida. Esta quiere decir que cada elemento medido cuenta con 500 IRF o A-scan. El elemento bajo estudio se encuentra enterrado en la mitad exacta del recorrido realizado por el posicionador. Esto quiere decir, que el posicionador realiza un barrido de 50 cm y el centro geométrico del elemento se encuentra a 25 cm. Todos los elementos se encuentran a una profundidad de 5 cm.

omo es conocido la exploración con tegnologias GPR busca describir a traves de imagenes lo que se encuentra bajo la superficie en estudio. Por esta razón, es necesario tomar esos 500 IRF de cada elemento medido para formar una imagen llamada B-scan, que no es mas que la descripción de la firma hiperbolica producida por las ondas electromagneticas al hacer contacto con el elemento de interes que se encuentra bajo la superficie.


## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
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
