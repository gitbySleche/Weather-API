from flask import Flask, request, redirect
from dotenv import load_dotenv
import json
import requests
import sys
import os

if len(sys.argv) == 2:
    
    city = sys.argv[1]
    try:
        
        load_dotenv()
        key = os.getenv('API_KEY')
        
        try:
            response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={key}')
        
        except requests.exceptions.ConnectionError:
            print('Error: No internet connection.')
            sys.exit(1)
    
    except FileNotFoundError:
        print('Error: File not found.')
        sys.exit(1)

    if response.status_code != 200:

        print(f'Error: {response.status_code}')
        sys.exit(1)
    
    data = response.json()

else:

    print('Input error. Intended usage: "python Weather_API.py <Location>"')
    sys.exit(1)

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

