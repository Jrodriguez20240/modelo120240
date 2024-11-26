
FROM python:3.10-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Flask
EXPOSE 8080

# Comando para ejecutar tu aplicación Flask
CMD ["gunicorn", "-b", ":8080", "ejecutar:app"]
