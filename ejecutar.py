# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 00:29:20 2024

@author: EAscritorio
"""
import os
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Carga el modelo
model = load_model('C:/Users/EAscritorio/Desktop/proyectogen/model_1.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    # Guardar la imagen en un directorio temporal
    img_path = os.path.join('C:/Users/EAscritorio/Desktop/proyectogen/imagenes', file.filename)
    file.save(img_path)

    # Cargar la imagen y realizar la predicción
    img = image.load_img(img_path, target_size=(218, 178))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)

    # Procesar la predicción
    gender = 'Hombre' if prediction[0][0] > 0.5 else 'Mujer'

    return f'Género: {gender}'

if __name__ == '__main__':
    app.run(debug=True)

