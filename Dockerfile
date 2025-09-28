# Usa una imagen base de Python
FROM python:3-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /programas/ingesta

# Instala las dependencias necesarias
RUN pip3 install boto3 mysql-connector-python

# Copia todo el contenido del directorio local al contenedor
COPY . .

# Establece el comando para ejecutar el script de Python al iniciar el contenedor
CMD ["python3", "./ingesta.py"]

