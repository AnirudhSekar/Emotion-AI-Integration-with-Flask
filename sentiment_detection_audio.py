import assemblyai as aai
import os
async def analyze_audio():
    aai.settings.api_key = "YOUR API KEY HERE"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("/Users/anirudhsekar/Desktop/Coding/SentimentAnalysis/audio.wav")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    return transcript.text
print(analyze_audio())