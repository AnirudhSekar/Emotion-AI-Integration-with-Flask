import assemblyai as aai
async def analyze_audio():
    aai.settings.api_key = "YOUR API KEY" 
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("PATH TO YOUR AUDIO.WAV FILE")
    return transcript.text
