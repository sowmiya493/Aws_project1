Lambda_function.py:

import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Product')

def lambda_handler(event, context):
    operation = event.get('operation')
    if operation == 'addProduct':
        return saveProduct(event)
    elif operation == 'updateProduct':
        return updateProduct(event)
    elif operation == 'getProducts':
        return getProducts()
    else: 
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }

def saveProduct(event):
    gmt_time = time.gmtime()
    now = time.strftime('%a, %d %b %Y %H:%M:%S', gmt_time)

    try:
        table.put_item(
            Item={
                'productCode': event['productCode'],
                'price': event['price'],
                'createdAt': now
            })
        return {
            'statusCode': 200,
            'body': json.dumps('Product with ProductCode: ' + event['productCode'] + ' created at ' + now)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

def updateProduct(event):
    productCode = event.get('productCode')
    price = event.get('price')
    new_createdAt = event.get('createdAt')  # Check if new createdAt value is provided

    if not productCode:
        return {
            'statusCode': 400,
            'body': json.dumps('ProductCode is required')
        }

    try:
        # Check if the product exists
        response = table.get_item(Key={'productCode': productCode})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps('Product with ProductCode: ' + productCode + ' not found')
            }

        # Update the product attributes
        update_expression = 'SET '
        expression_attribute_values = {}

        if price is not None:
            update_expression += '#price = :price'
            expression_attribute_values[':price'] = price
            table.update_item(
                Key={'productCode': productCode},
                UpdateExpression=update_expression,
                ExpressionAttributeNames={'#price': 'price'},
                ExpressionAttributeValues=expression_attribute_values
            )

        if new_createdAt:
            update_expression += ', #createdAt = :createdAt'
            expression_attribute_values[':createdAt'] = new_createdAt
            table.update_item(
                Key={'productCode': productCode},
                UpdateExpression=update_expression,
                ExpressionAttributeNames={'#createdAt': 'createdAt'},
                ExpressionAttributeValues=expression_attribute_values
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Product with ProductCode: ' + productCode + ' updated')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

def getProducts():
    try:
        response = table.scan()
        items = response['Items']
        return {
            'statusCode': 200,
            'body': json.dumps(items),
            'headers': {
                'Content-Type': 'application/json',
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
