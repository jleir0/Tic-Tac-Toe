# Usa una imagen base de Python
FROM python:3.8

# Copia todo el contenido de la carpeta src al directorio de trabajo en la imagen
COPY src/ /src/

# Establece el directorio de trabajo en /src
WORKDIR /src

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Especifica el comando de inicio
CMD ["python", "app.py"]
