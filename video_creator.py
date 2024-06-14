from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

class VideoCreator:
    def __init__(self, font_path):
        self.font_path = font_path

    def create_video(self, background_image, quote, music_file, quote_audio_file, output_file):
        img = Image.open(background_image)
        draw = ImageDraw.Draw(img)
        
        font = ImageFont.truetype(self.font_path, 50)
        text_width, text_height = draw.textsize(quote, font=font)
        width, height = img.size
        text_x = (width - text_width) / 2
        text_y = (height - text_height) / 2
        draw.text((text_x, text_y), quote, font=font, fill="white")
        
        edited_image_path = "edited_background.png"
        img.save(edited_image_path)
        
        video_clip = ImageClip(edited_image_path).set_duration(10)
        audio_clip = AudioFileClip(music_file).subclip(0, 10)
        quote_audio_clip = AudioFileClip(quote_audio_file).subclip(0, 8).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
        final_audio = CompositeAudioClip([audio_clip, quote_audio_clip.set_start(1)])
        
        video_clip = video_clip.set_audio(final_audio)
        video_clip.write_videofile(output_file, fps=24)
