import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import time
import os  # to remove created audio files


# checks if the spoken phrase contains words from the terms list
def there_exists(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()  # initialise a recogniser

mic_on = True
def command(command):
    global mic_on
    mic_on = command
    print('mic is OFF')


# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source
        print('mic is ON')
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="pl-PL")  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak('Nie rozumiem, proszę powtórzyć')
        except sr.RequestError:
            speak('Przepraszam. Serwis nie działa')  # error: recognizer is not connected
        print(">> {}".format(voice_data.lower()))  # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='pl')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print("kiri: {}".format(audio_string))  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data, steps_array_voice):
    # 1: krok 1
    if len(steps_array_voice) != 0 and there_exists(['hej szef', 'halo szef'], voice_data)\
                                   and there_exists(['krok 1', 'krok pierwszy', '1 krok', 'pierwszy krok'], voice_data):
        krok = 'czytam krok pierwszy: ' + steps_array_voice[0]
        speak(krok)

    # 1: krok 2
    if len(steps_array_voice) > 1 and there_exists(['hej szef', 'halo szef'], voice_data)\
                                  and there_exists(['krok 2', 'krok drugi', '2 krok', 'drugi krok'], voice_data):
        krok = 'czytam krok drugi: ' + steps_array_voice[1]
        speak(krok)

    # 1: krok 3
    if len(steps_array_voice) > 2 and there_exists(['hej szef', 'halo szef'], voice_data)\
                                  and there_exists(['krok 3','krok trzeci', '3 krok', 'trzeci krok'], voice_data):
        krok = 'czytam krok trzeci: ' + steps_array_voice[2]
        speak(krok)

    # 1: krok 4
    if len(steps_array_voice) > 3 and there_exists(['hej szef', 'halo szef'], voice_data)\
                                  and there_exists(['krok 4', 'krok czwarty', '4 krok', 'czwarty krok'], voice_data):
        krok = 'czytam krok czwarty: ' + steps_array_voice[3]
        speak(krok)

    # 1: krok 5
    if len(steps_array_voice) > 4 and there_exists(['hej szef', 'halo szef'], voice_data)\
                                  and there_exists(['krok 5', 'krok piąty', '5 krok', 'piąty krok'], voice_data):
        krok = 'czytam krok piąty: ' + steps_array_voice[4]
        speak(krok)

    if there_exists(["wyłącz sterowanie głosowe", "goodbye"], voice_data):
        speak("Sterowanie głosowe zostało wyłączone.")
        command(False)


def start_voice_assistant(steps_array_voice):
    time.sleep(1)
    while mic_on:
        print('while working')
        mic_data = record_audio()  # get the voice input
        respond(mic_data, steps_array_voice)  # respond
