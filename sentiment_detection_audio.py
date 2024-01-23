import assemblyai as aai
import os
def analyze_audio():
    aai.settings.api_key = "24852772dd4b4e43a8c7591c49466337"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("/Users/anirudhsekar/Desktop/Coding/SentimentAnalysis/audio.wav")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    return transcript.text
print(analyze_audio())