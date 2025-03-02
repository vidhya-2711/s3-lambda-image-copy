import json
import boto3

s3 = boto3.client('s3')  # Use boto3 client instead of resource

def lambda_handler(event, context):
    print("Event:", json.dumps(event, indent=2))

    for record in event['Records']:
        print("Processing Record:", json.dumps(record, indent=2))

        source_bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        destination_bucket = source_bucket + "-copy"  # Ensure correct destination bucket name

        copy_source = {
            'Bucket': source_bucket,
            'Key': file_key
        }

        try:
            s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=file_key)
            print(f"File '{file_key}' copied from '{source_bucket}' to '{destination_bucket}' successfully.")
        except Exception as e:
            print(f"Error copying file: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }


























