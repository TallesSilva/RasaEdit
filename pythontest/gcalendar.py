from __future__ import print_function
import datetime
import pickle
import os.path
from os import remove
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from fakes import get_fake_date

DEFAULT_VISIT_TIME = 1  # in minutes
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS = 'scheduler_agent/credentials.json'

def clean_up(exception):
    print("Uma exceção foi lançada:\n{} Os arquivos de credenciais foram "
          "apagados. O arquivo `credentials.json` deve ser buscado novamente"
          "".format(exception))
    remove('token.pickle')
    setup_interface()
        

def setup_interface():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except Exception as ex:
        clean_up(ex)
    
def fill_event_document(customer: dict,
                       start_date: str,
                       end_date: str):
    return {
        'summary': 'Visita técnica',
        'location': None,
        'description': 'Visita técnica à casa de um ',
        'start': {
            'dateTime': start_date,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_date,
            'timeZone': 'America/Sao_Paulo',  
        },
    }
    
def create_event(customer):
    service = setup_interface()
    
    start_date = get_fake_date()
    end_date = start_date + datetime.timedelta(hours=DEFAULT_VISIT_TIME)
    
    start_date = start_date.strftime("%Y-%m-%dT%H:%M:%S")
    end_date = end_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    event = fill_event_document(customer, start_date, end_date)
    try:
        service.events().insert(calendarId='primary', body=event).execute()
    except Exception as ex:
        raise 

create_event('joao')