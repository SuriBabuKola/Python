import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='demo-s3-bucket-using-boto3',
)

print("Bucket created successfully:", response)