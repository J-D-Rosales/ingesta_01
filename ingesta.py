import boto3

ficheroUpload = "data.csv"
nombreBucket = "jdrosales"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload,"ingesta/", ficheroUpload)
print(response)

print("Ingesta completada")