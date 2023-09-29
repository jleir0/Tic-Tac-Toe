# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia todo el contenido de la carpeta src al directorio de trabajo en la imagen
COPY src/ /app/

# Especifica el comando de inicio
CMD ["python", "app.py"]
