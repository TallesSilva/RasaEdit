from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests



SCOPES = ['https://www.googleapis.com/auth/calendar.settings.readonly']

    
def insert_datetime():
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

    
    event = {
        'summary': 'Evento Google API',
        'location': 'Minha casa',
        'description': 'Teste de inserção com o googleApi',
        'start': {
            'dateTime': '2019-09-17T09:00:00-07:00',
            'timeZone': 'America/Sao Paulo',
        },
        'end': {
            'dateTime': '2019-09-17T15:00:00-07:00',
            'timeZone': 'America/Sao Paulo',  
        },
    }
    print('event created')
    try:
        service.events().insert(calendarId='primary', body=event).execute()
        return "OK"
    except Exception as falha:
        logger.erro(falha.__name__)
        logger.erro("falha ao criar timetable sem a data: {}".format(str(falha)))  


def get_calendar():
    r = requests.get("http://192.168.1.3:8080/timetables/")
    print(r.json())

