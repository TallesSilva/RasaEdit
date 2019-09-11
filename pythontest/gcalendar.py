from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

scopes = ['https://www.googleapis.com/auth/calendar']

def config():
    creds = None
    service = None
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)

def insert_datetime(y,m,d,th,tm,ts,td):
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