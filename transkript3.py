import speech_recognition as sr
import os
from datetime import datetime

def mainTranskript(minute):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    transkript_folder = os.path.join(desktop_path, "transkript")
    if not os.path.exists(transkript_folder):
        os.makedirs(transkript_folder)

    today_date = datetime.now().strftime("%Y-%m-%d")
    
    transkript_file = f"{today_date}.txt"

    print("transkript started")
    for i in range(minute):
        ses_dosyasi = f'output{i}.wav'
        ses = sr.AudioFile(ses_dosyasi)
        r = sr.Recognizer()
        with ses as source:
            audio = r.record(source)
        try:
            metin = r.recognize_google(audio, language="tr-TR")
            print("Ses dosyasından çevrilen metin:")
            print(metin)
            with open(os.path.join(transkript_folder, transkript_file), "a") as file:
                file.write(metin + " ")
            os.remove(ses_dosyasi)
        except sr.UnknownValueError:
            print("Ses dosyası anlaşılamadı")
        except sr.RequestError as e:
            print("Sorgu hatası; {0}".format(e))
    print("transkript ended")

