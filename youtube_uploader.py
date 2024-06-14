import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class YouTubeUploader:
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    def __init__(self, client_secrets_file):
        self.client_secrets_file = client_secrets_file
        self.service = self.get_authenticated_service()

    def get_authenticated_service(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.client_secrets_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return build('youtube', 'v3', credentials=creds)

    def upload_video(self, file_path, title, description, category_id, tags):
        request_body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': category_id
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False,
            }
        }

        media_file = MediaFileUpload(file_path, chunksize=-1, resumable=True)
        request = self.service.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media_file
        )

        response = request.execute()
        print(f"Uploaded video ID: {response['id']}")
