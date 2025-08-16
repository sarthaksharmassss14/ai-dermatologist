from dotenv import load_dotenv
load_dotenv()

import os
from gtts import gTTS
from elevenlabs import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# gTTS
def text_to_speech_with_gtts(input_text: str, output_filepath: str) -> str:
    """Generate speech using gTTS and return the saved file path."""
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    return output_filepath


# ElevenLabs
def text_to_speech_with_elevenlabs(input_text: str, output_filepath: str) -> str:
    """Generate speech using ElevenLabs and return the saved file path."""
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL", 
        model_id="eleven_turbo_v2",
        text=input_text
    )

    
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    return output_filepath



if __name__ == "__main__":
    input_text = "Hi this is AI Dermatologist ready for your help"
    print("Saved with gTTS:", text_to_speech_with_gtts(input_text, "gtts_testing.mp3"))
    print("Saved with ElevenLabs:", text_to_speech_with_elevenlabs(input_text, "elevenlabs_testing.mp3"))

