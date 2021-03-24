# first thing first, pip3 install SpeechRecognition

import speech_recognition as sr

# check version to see if installed
print(sr.__version__)

# recognizer instance to recognize speech from an audio source
r = sr.Recognizer()


# opens the audio file in dir, reads content, stores data in audioSource
# instance then records data from entire file into AudioData instance
harvard = sr.AudioFile("*.wav")
with harvard as audioSource:
    # handles noise by reading first second of file stream and calibrating recognizer to that noise level
    # r.adjust_for_ambient_noise(audioSource)
    audio = r.record(audioSource)

    
# confirm AudioData instance exists
print(type(audio))

# there are many speechrecognition api's but I chose google (not google_cloud) because its the quickest to get started (don't need api keys)

# provide audio_data (AudioData instance) in recognizer_*() call --> supports wav, aiff, aiff-c, and flac
# 'show_all=True' will return a dictionary with key-'alternative' that points to a list of possible transcripts
print(r.recognize_google(audio))
