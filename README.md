# Video Creator Application

This application automates the creation of videos using a background image, a quote, background music, and the audio version of the quote. It can also upload the created videos to YouTube.

## Features
- Generate audio from text using Google Text-to-Speech.
- Create a video with the generated audio, background image, and background music.
- Optionally upload the video to YouTube.

## Setup

### Prerequisites
1. **Google Cloud Project**:
   - Enable the Text-to-Speech API.
   - Create a Service Account and download the JSON key file.
2. **YouTube Data API**:
   - Enable the YouTube Data API v3.
   - Create OAuth 2.0 credentials and download the client secrets JSON file.

### Installation

1. Clone this repository.
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Place your service account JSON key and OAuth client secrets JSON file in the project directory as shown below:
    ```
    video_creator/
    ├── audio_generator.py
    ├── video_creator.py
    ├── youtube_uploader.py
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── service_account.json      # Place your service account JSON key here
    └── client_secrets.json       # Place your OAuth client secrets JSON file here
    ```

### Configuration

Update the paths in `main.py` to point to your service account JSON key and client secrets JSON file:
```python
SERVICE_ACCOUNT_JSON = 'service_account.json'
CLIENT_SECRETS_FILE = 'client_secrets.json'
FONT_PATH = 'arial.ttf'
```
4. Run main.py
