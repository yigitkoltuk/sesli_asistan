import os
import time

import playsound2
import speech_recognition as sr
from gtts import gTTS
import requests


print("Birşeyler söyle")
def speak(text):
    tts = gTTS(text=text, lang="tr")
    filename = "voice.mp3"
    tts.save(filename)
    playsound2.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        said = ''

        try:
            said = r.recognize_google(audio, language="tr-tr")
            print(said)
        except Exception as e:
            print("ne dediğiniz anlamadım")

    return said


text = get_audio()

if "Merhaba" in text:
    speak("Merhaba ben  geliştirilmekte olan bir sesli asistanım şu anda sadece merhaba ve hava durumu komutlarına cevap verebiliyorum")



if "hava durumu" in text:

    city = 'İstanbul'
    API_key = '4855bf4f1d70b03a357e7c3022d97f54'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city }&appid={API_key}')
    weatherData = response.json()
    skyDescription = weatherData['weather'][0]['description']
    cityName = weatherData['name']
    skyTypes = ['clear sky', 'few clouds', 'overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain',
                'rain', 'thunderstorm', 'snow', 'mist']
    skyTypesTR = ['Güneşli', 'Az Bulutlu', 'Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu',
                  'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    for i in range(len(skyTypes)):
        if skyDescription == skyTypes[i]:
            skyDescription = skyTypesTR[i]
    temp = int((weatherData['main']['temp'] - 273.15))  # Genel sıcaklık
    feels_temp = int((weatherData['main']['feels_like'] - 273.15))  # hissedilen

    speak(f"bugün hava {skyDescription} ve {temp}derece ama hissedilen sıcaklık {feels_temp}")

