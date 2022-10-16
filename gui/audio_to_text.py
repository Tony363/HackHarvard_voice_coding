from google.cloud import speech

def giveText(file_name):
    client = speech.SpeechClient.from_service_account_file('key.json')

    with open(file_name,'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)

    config = speech.RecognitionConfig(
        sample_rate_hertz = 8000,
        enable_automatic_punctuation = True,
        language_code = 'en-US'
    )

    response = client.recognize(
        config = config,
        audio =  audio_file
    )

    for result in response.results:
        return result.alternatives

if __name__ == "__main__":
    print(giveText("output.wav"))