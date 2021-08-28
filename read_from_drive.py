from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/docs-automation-324207-0769ba6256c2.json")

service = build('drive', 'v3', credentials=creds)

def read_from_drive(folder_id):
    query = f"'{folder_id}' in parents"
    response = service.files().list(q=query).execute()

    items = response.get('files')

    l=[]
    for item in items:
        l.append(items)
        print(item)

    return l

