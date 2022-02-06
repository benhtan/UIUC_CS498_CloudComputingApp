import json
import boto3

def lambda_handler(event, context):
    # print(event)
    source = event['currentIntent']['slots']['Source']
    destination = event['currentIntent']['slots']['Destination']
    print(f'{source}->{destination}')
    
    # DynamoDB
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table_CS498_MP3_Distance = dynamodb.Table('CS498-MP3-Distance')
    
    response = None
    try:
        route = table_CS498_MP3_Distance.get_item(Key={'route':f'{source}->{destination}'})['Item']
        print(f'route: {route}')

        response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": route['distance']
            },
        }
    }
    except Exception as e:
        print(e)
        response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": "Something is wrong"
            },
        }
    }
    
    print(f'response: {response}')
    return response