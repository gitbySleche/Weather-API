from flask import Flask, jsonify
from dotenv import load_dotenv
import redis
from redis.exceptions import ConnectionError as RedisConnectionError
import json
import requests
import sys
import os

app = Flask(__name__)

try:
    load_dotenv('key.env')
    key = os.getenv('API_KEY')

except FileNotFoundError:
    print('Error: File not found.')
    sys.exit(1)

@app.route('/<location>')
def Weather_API(location):
    
    try: # Check Redis to see if the location is stored in cache memory.
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        r.ping()
        data = r.get(location)
        if data:
            data = json.loads(data)  # convert string back to dict
            return jsonify(data)

    except RedisConnectionError:
        return jsonify({'error': 'Could not connect to Redis.'}), 500
    
    if data == None: #If Redis has no cached data on the specified location then do the VisualCrossing API call.   
        try:
            response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={key}')

            if response.status_code != 200:
                return jsonify({'error': f'API error: {response.status_code}'}), 502

            data = response.json()
            r.set(location, json.dumps(data), ex=1296000) #Stores data returned in Redis as an entry.
            return jsonify(data)

        except requests.exceptions.ConnectionError:
            return jsonify({'error': 'No internet connection.'}), 503
    
if __name__ == '__main__':
    app.run(debug=True)