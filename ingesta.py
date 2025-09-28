import mysql.connector
import csv
import boto3

# Conectar a la base de datos MySQL en MV1, usando el nuevo puerto 3307
db_connection = mysql.connector.connect(
    host="172.31.19.170",  # IP privada de MV1
    user="root",          # Usuario de MySQL
    password="123",  # Contraseña de root de MySQL
    database="ingesta",  # Nombre de la base de datos
    port=3307  # Puerto actualizado
)
cursor = db_connection.cursor()

# Consultar los registros de la tabla
cursor.execute("SELECT * FROM empleados")
registros = cursor.fetchall()

# Guardar los registros en un archivo CSV
with open("empleados.csv", mode="w", newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow([i[0] for i in cursor.description])  # Escribir los encabezados
    writer.writerows(registros)

print("Datos guardados en empleados.csv")

# Subir el archivo CSV a S3
ficheroUpload = "empleados.csv"
nombreBucket = "jdrosales"  # Reemplaza por el nombre de tu bucket
s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "ingesta/" + ficheroUpload)
print(response)

print("Ingesta completada")

