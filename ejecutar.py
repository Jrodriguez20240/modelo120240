# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:29:20 2024

@author: EAscritorio
"""
from flask import Flask, request, render_template, redirect, url_for
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)

# Cargar el modelo de predicción
model = tf.keras.models.load_model('model_1.keras')

# Carpeta donde se guardarán temporalmente las imágenes
UPLOAD_FOLDER = 'imagenes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la predicción
@app.route('/predict', methods=['POST'])
def predict():
    # Verificar si se ha subido un archivo
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('index'))

    # Guardar la imagen subida en la carpeta de uploads temporales
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Preprocesar la imagen para el modelo
        img = image.load_img(file_path, target_size=(218, 178))  # Ajustar al tamaño del modelo
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Realizar la predicción
        predictions = model.predict(img_array)
        gender = "Mujer" if predictions[0][0] > 0.5 else "Hombre"

        # Generar la URL de la imagen cargada para mostrarla en result.html
        image_url = url_for('static', filename='imagenes/' + file.filename)

        # Renderizar la plantilla de resultados con la imagen y la predicción
        return render_template('result.html', prediction=gender, image_url=image_url)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
