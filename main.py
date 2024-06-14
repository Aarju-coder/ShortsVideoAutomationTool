import os
from audio_generator.py import AudioGenerator
from video_creator.py import VideoCreator
from youtube_uploader.py import YouTubeUploader

SERVICE_ACCOUNT_JSON = 'path_to_your_service_account_key.json'
CLIENT_SECRETS_FILE = 'client_secrets.json'
FONT_PATH = 'arial.ttf'

def main():
    # Inputs
    background_image = "background.jpg"
    quote = "This is a sample quote."
    music_file = "background_music.mp3"
    output_video_file = "output_video.mp4"
    quote_audio_file = "quote_audio.mp3"
    upload_to_youtube = True  # Change to False if you don't want to upload
    youtube_details = {
        "title": "My YouTube Shorts Video",
        "description": "Description of the video",
        "category_id": "22",
        "tags": ["shorts", "video", "example"]
    }

    # Generate audio for the quote
    audio_generator = AudioGenerator(SERVICE_ACCOUNT_JSON)
    audio_generator.text_to_speech(quote, quote_audio_file)

    # Create video
    video_creator = VideoCreator(FONT_PATH)
    video_creator.create_video(background_image, quote, music_file, quote_audio_file, output_video_file)

    # Optionally upload to YouTube
    if upload_to_youtube:
        youtube_uploader = YouTubeUploader(CLIENT_SECRETS_FILE)
        youtube_uploader.upload_video(
            output_video_file,
            youtube_details["title"],
            youtube_details["description"],
            youtube_details["category_id"],
            youtube_details["tags"]
        )

if __name__ == "__main__":
    main()
