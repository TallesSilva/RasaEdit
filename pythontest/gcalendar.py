from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def config():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

def insert_datetime(y,m,d,th,tm,ts,td):
    #chamar os parametros creds e services da função de configuraçao
    start_time = datetime(y, m, d, th, tm, ts)
    end_time = start_time + timedelta(hours=td)
    timezone = 'Asia/Kolkata'
    event = {
        'summary': 'IPL Final 2019',
        'location': 'Hyderabad',
        'description': 'MI vs TBD',
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }  
    print('event created')
    return service.events().insert(calendarId='primary', body=event).execute()

config()