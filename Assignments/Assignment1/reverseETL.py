from __future__ import print_function
import os.path
import psycopg2
import datetime

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


conn = psycopg2.connect(database="customerDB",
                        host="localhost",
                        user="postgres",
                        password="080921",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * from customer")

result_data = cursor.fetchall()
values_list = []
for data in result_data:
    date = data[4].strftime("%Y-%M-%D")
    values_update = data[:-1] + (date,)
    values_list.append(list(values_update))
def create(title):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'API_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        retlService = build('sheets', 'v4', credentials=creds)
        spreadsheet_data = [
                            {"range": "Sheet1!A1",  
                            "values": [["customer_id",'first_name','last_name','email','created_on']] 
                            },
                            {
                            "range": "Sheet1!A2",  
                            "values": values_list
                            }
                        ]
        spreadsheetID =  "14aOGmufaPBQAvs2TMO3OPfz-4doyvsp72yPSm1L4K_I"
        spreadsheet = {
            'valueInputOption' :  'RAW',
            'data' : spreadsheet_data
        }
        spreadsheet = retlService.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheetID, body=spreadsheet).execute()
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        return error


if __name__ == '__main__':
    create("EDS-assignment-1")