# Proyecto de predicción degénero con Machine Learning

Este proyecto utiliza un modelo de Machine Learning para predecir el género de una persona basado en una imagen de su rostro.
El modelo ha sido entrenado previamente y se sirve mediante una API desarrollada con Flask. Esta API está alojada en **Google Cloud Run**
para ser accesible desde cualquier lugar a través de un enlace.

## Descripción

El propósito de este proyecto es proporcionar una solución en la que los usuarios puedan cargar una imagen de una persona, y la API devolverá la predicción del género de la persona (masculino o femenino).
El modelo se encuentra en el archivo `model_1.keras` y es cargado en el servidor para realizar las predicciones.

La API está construida con **Flask** y se desplegó en **Google Cloud** para que sea accesible desde cualquier lugar. 
Además, el proyecto también incluye una interfaz web simple desarrollada en HTML para permitir a los usuarios cargar imágenes y recibir resultados en tiempo real.

## Dependencias

Para que el proyecto funcione correctamente, asegúrate de tener las siguientes dependencias instaladas:

- Python 3.9+
- Flask
- TensorFlow
- Gunicorn (para producción)
- Entre otros paquetes necesarios para el funcionamiento del modelo
Puedes instalar todas las dependencias necesarias utilizando el archivo `requirements.txt` con el siguiente comando:
pip install -r requirements.txt
## Despliegue

# 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

git clone https://github.com/tu-usuario/modelo120240.git
cd modelo120240
# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  #  Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Hacer una prueba local
python app.py

# 5. Desplegar en google cloud

# 5.1. Construir la imágen docker
docker build -t gcr.io/proyecto-120240/proyecto-prediccion-genero  .

# 5.2. Subir la imagen a google cloud (Google Container Registry)
docker push gcr.io/proyecto-120240/proyecto-prediccion-genero

# 5.3 Desplegar en google cloud run
gcloud run deploy --image gcr.io/tu-proyecto-id/proyecto-prediccion-genero --platform managed --region us-central1 --allow-unauthenticated

# 6. A partir del enlace generado, acceder.







