# Despliegue de modelos

## Infraestructura 

- **Nombre del modelo:** Landmine detection using GPR data - Statistical Approach with Feature Extraction
- **Plataforma de despliegue:** El modelo es desplegado en FastAPI
- **Requisitos técnicos:** 
    -Versión de Python: 3.11.3
    -Librerias: FasAPI-0.98, json-2.0.9, numpy-1.24.4, sklearn-1.2.2, joblib-1.2.0,plotly-5.13.1, scipy-1.10.1
    -Software: Ubuntu 18.04.6 LTS
    -Hardware: CPU: Intel Core i7-8750H 2.20 GHz, GPU NVIDIA Gforce 1050, RAM 32 GB
- **Requisitos de seguridad:** no se requiere
- **Diagrama de arquitectura:** 
![Texto alternativo](https://github.com/Fabianunal/Proyecto_msdl6/blob/master/docs/deployment/Arq.PNG)
## Código de despliegue

- **Archivo principal:** DeploymentAPI.py
- **Rutas de acceso a los archivos:** https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/Deployment/deploymentapi.py, https://github.com/Fabianunal/Proyecto_msdl6/blob/master/scripts/Deployment/main.py, https://github.com/Fabianunal/Proyecto_msdl6/tree/master/scripts/Deployment


## Documentación del despliegue

- **Instrucciones de instalación:** El proceso de instalación para desplegar un modelo de Machine Learning en FastAPI se utilizan los siguientes pasos:
- Clona el repositorio de GitHub
- Crea y activa un entorno virtual
- Instala las dependencias necesarias
- Descarga los archivos del modelo
- Configura FastAPI usa un archivo main.py y define tu aplicación FastAPI. Puedes usar el siguiente código como punto de partida
- Inicia el servidor FastAPI
- 
- **Instrucciones de configuración:**
- Los datos son un vector que previamente se a realizado el proceso de estracción de caracteristicas.
  
- **Instrucciones de uso:** Estas se finalizaran cuando el midelo se entregue por completo.
  
- **Instrucciones de mantenimiento:** Por ahora no aplica. 
