import requests

token = ""
with open('credentials/token.txt', 'r') as file:
    token = file.read().strip()

print(token)

# Use the access token to make a request to the Google Calendar API
calendar_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
headers = {
    'Authorization': f'Bearer {token}',
}

response = requests.get(calendar_url, headers=headers)
response_info = response.json()
events = response.json().get('items', [])

if not events:
    print('No upcoming events found.')
else:
    print('Upcoming events:')
    for event in events:
        if 'start' in event and 'dateTime' in event['start']:
            start = event['start'].get('dateTime')
            print(f'{start} - {event["summary"]}' + ' id: ' + event['id'])
        elif "summary" in event:
            print(event["summary"] + ' id: ' + event['id'])
        else:
            print(event['id'])