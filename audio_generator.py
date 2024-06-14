from google.cloud import texttospeech

class AudioGenerator:
    def __init__(self, service_account_json):
        self.client = texttospeech.TextToSpeechClient.from_service_account_json(service_account_json)

    def text_to_speech(self, text, output_audio_file):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config)
        
        with open(output_audio_file, 'wb') as out:
            out.write(response.audio_content)
            print(f'Audio content written to file {output_audio_file}')
