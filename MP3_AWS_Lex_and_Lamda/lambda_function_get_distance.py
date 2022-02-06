import json
import boto3

def lambda_handler(event, context):
    print(event) 
    # DynamoDB
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table_CS498_MP3_Distance = dynamodb.Table('CS498-MP3-Distance')
    
    try:
        route = table_CS498_MP3_Distance.get_item(Key={'source': 'Chicago', 'destination': 'Urbana'})
        print(route['distance'])

        return {
        'statusCode': 200,
        'distance': route['distance'],
        'body': 'Success'
        }
    except Exception as e:
        print(e)
        return {
        'statusCode': 500,
        'body': 'Error Reading'
        }