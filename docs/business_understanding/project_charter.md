# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Detección de Artefactos Explosivos Improvisados Usando Técnicas de Machine Learning

## Objetivo del Proyecto

En el marco de este proyecto se utiliza un dataset de medidas realizados por un sistema de penetración terrestre (GPR por sus siglas en inglés) ubicado en el campus de la Universidad Nacional de Colombia sede Bogotá. Las medidas tomadas por este sistema GPR corresponden a una serie de artefactos explosivos improvisados (IED por sus siglas en inglés) enterrados, junto con diversos elementos canónicos (cilindros) enterrados de diferentes materiales y dimensiones que serán etiquetados como Clutter. El objetivo de este proyecto es clasificar IEDs de Clutter (no IED) mediante el uso de técnicas de Machine Learning.

Las medidas se realizan desplazando el dispositivo GPR junto con los sensores (antenas) en un sistema de posicionamiento a una velocidad de 1 cm/s sobre el elemento canónico enterrado, obteniendo 500 IRF (Impulse Respond Function) en la zona medida. Esta quiere decir que cada elemento medido cuenta con 500 IRF o A-scan. El elemento bajo estudio se encuentra enterrado en la mitad exacta del recorrido realizado por el posicionador. Esto quiere decir, que el posicionador realiza un barrido de 50 cm y el centro geométrico del elemento se encuentra a 25 cm. Todos los elementos se encuentran a una profundidad de 5 cm.

omo es conocido la exploración con tegnologias GPR busca describir a traves de imagenes lo que se encuentra bajo la superficie en estudio. Por esta razón, es necesario tomar esos 500 IRF de cada elemento medido para formar una imagen llamada B-scan, que no es mas que la descripción de la firma hiperbolica producida por las ondas electromagneticas al hacer contacto con el elemento de interes que se encuentra bajo la superficie.
## Alcance del Proyecto.  

Los IEDs considerados en el marco de este proyecto están compuestos por una jeringa que actúa como interruptor, cables, batería, detonador, el sustituto del explosivo ANFO y por ultimo contenido metálico conocido como metralla. Es importante resaltar que los IEDs no contienen explosivos, estos son reemplazados por materiales sustitutos que poseen la misma constante dieléctrica, en este caso se cuenta con un material rico en nitrógeno como sustituto del ANFO con una permitividad de 3.9.

### Incluye:

- [Descripción de los datos disponibles]
En el marco de este proyecto se utiliza un dataset de medidas realizados por un sistema de penetracion terrestre (GPR por sus siglas en ingles) ubicado en el campus de la Universidad Nacional de Colombia sede Bogota. Las medidas tomadas por este dispositivo corresponden a una serie de IEDs y de elementos canonicos enterrados (cilindros) de diferentes materiales y diferentes dimensiones.
- [Descripción de los resultados esperados]
El proposito de las medidas realizadas para construir este dataset con elementos canonicos e IEDs es determinar la capacidad del sistema GPR (ver figura 4) en detectar elementos con diferentes permitividades y dimensiones (IEDs y no IEDs). En ese sentido, se implementa un clasificador entre IEDs y no IEDs sobre los A-scan del dataset.
- [Criterios de éxito del proyecto]
Claridad en la definición de objetivos.
Utilización de una metodología.
Precisión en la planificación.
Compromiso de los participantes.
El presupuesto disponible.
El tiempo de ejecución.

### Excluye:

- Diferenciar entre clases de IEDs ya que estos pueden ser contruidos en cualquier recipiente comercial o en tubos de PVC.

## Metodología

La metodologia adoptada es: TDSP
Entendimiento del negocio
Adquisición y entendimineto de los datos.
Modelamiento.
Despliegue.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 5 de junio al 11 de junio |
| Entendimiento de los datos | 1 semanas | del 5 de mayo al 11 de junio |
| Modelamiento y extracción de características | 1 semanas | del 12 de junio al 18 de junio |
| Despliegue | 1 semanas | del 19 de junio al 25 de junio |
| Evaluación y entrega final | 3 semanas | del 26 de junio al 30 de junio |



## Equipo del Proyecto

- Felix Vega - Lider del proyecto
- Cesar Pedraza - Gerente del proyecto
- Alejandro Rangel Retavisca - Data scientist
- Eder Fabian Ruiz - Data scientist

## Presupuesto


| Item | Cost (USD) |
|------|---------|
| Technical Staff | $ 187.824 |
| Materials and equipment | $25.133 |
| Technological services and tests | $15.053 | 
|  Total |  $228.010 | 


## Stakeholders

- Luciano Prado - Senior Researcher - TII
- Sultan Abughazal - Associate Researcher - TII
- Revisores de los entregables


## Aprobaciones

- Cesar Pedraza - Gerente del proyecto

