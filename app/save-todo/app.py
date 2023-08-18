import json
import boto3
import uuid


def lambda_handler(event, context):
    print("event")
    print(event)
    print(event["body"])

    data = json.loads(event["body"])
    print(data["message"])

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Todo")
    table.put_item(Item={
        "id": str(uuid.uuid4()),
        "message": data["message"]
    })

    return {
        "statusCode": 204
    }
