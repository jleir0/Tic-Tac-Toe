# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido de la carpeta src al directorio de trabajo en la imagen
COPY src/ /app/

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código fuente de la aplicación al contenedor
COPY . .

# Especifica el comando de inicio
CMD ["python", "app.py"]
