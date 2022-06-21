import os
import logging

import boto3
from flask import Flask, jsonify, make_response, request
from myapi import config

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

if config.IS_OFFLINE:
    dynamodb_client = boto3.client(
        'dynamodb', region_name=config.REGION_NAME, endpoint_url=f'http://{config.DB_HOST}:{config.DB_PORT}'
    )
else:
    dynamodb_client = boto3.client('dynamodb')

USERS_TABLE = config.DYNAMODB_TABLE


@app.route('/')
def hello():
    return "OK", 200


@app.route('/users/<string:user_id>')
def get_user(user_id):
    app.logger.info(f"Example log for /users/{user_id}")
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )


@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provide both "userId" and "name"'}), 400

    dynamodb_client.put_item(
        TableName=USERS_TABLE, Item={'userId': {'S': str(user_id)}, 'name': {'S': name}}
    )

    return jsonify({'userId': user_id, 'name': name})


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    print("== Running in debug mode ==")
    app.run(host=config.HOST, port=config.PORT, debug=True)
