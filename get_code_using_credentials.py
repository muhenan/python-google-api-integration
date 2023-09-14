import json
import webbrowser

# Load OAuth 2.0 credentials from JSON file
credentials_file = 'credentials/client_secret.json'
credentials = json.load(open(credentials_file))

# Pretty-print the credentials dictionary
formatted_credentials = json.dumps(credentials, indent=4)
print("OAuth 2.0 Credentials:")
print(formatted_credentials)

credentials = credentials['web']

# Define the scope for accessing Google Calendar data
scope = 'https://www.googleapis.com/auth/calendar'
redirect_uri = 'http://localhost:3000'
auth_url = credentials["auth_uri"]
auth_params = {
    'client_id': credentials['client_id'],
    'redirect_uri': redirect_uri,
    'scope': scope,
    'response_type': 'code',  # Request an authorization code
}

authorization_url = f'{auth_url}?{"&".join(f"{key}={value}" for key, value in auth_params.items())}'

# Open a web browser to the authorization URL
webbrowser.open(authorization_url)

# Request an access token
# response = requests.post(token_url, data=token_data)
# token_info = response.json()
# print(token_info)

print("hello world")
