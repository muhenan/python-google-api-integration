import json
import requests

# Load OAuth 2.0 credentials from JSON file
credentials_file = 'credentials/client_secret.json'
credentials = json.load(open(credentials_file))
formatted_credentials = json.dumps(credentials, indent=4)
credentials = credentials['web']

code = ""
with open('credentials/code.txt', 'r') as file:
    code = file.read().strip()

# Define the token request parameters
token_data = {
    'client_id': credentials['client_id'],
    'client_secret': credentials['client_secret'],
    'code': code,
    'redirect_uri': 'http://localhost:3000',  # Should match your redirect_uri
    'grant_type': 'authorization_code',
}

response = requests.post(credentials['token_uri'], data=token_data)
access_token = ""

token_info = response.json()
access_token = token_info['access_token']

print(access_token)

with open('credentials/token.txt', 'w') as file:
    file.write(access_token)

print("hello")