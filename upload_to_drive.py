import json
import requests

with open ("credentials/google_access_token.txt","r") as f:
    google_access_token = f.read()

def upload_to_drive(folder_id,folder,filename):

    filename = filename+".docx"

    headers = {"Authorization": "Bearer "+google_access_token}
    para = {
        "name": filename,
        "parents": folder_id.split()
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(folder+"/"+filename, "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)
