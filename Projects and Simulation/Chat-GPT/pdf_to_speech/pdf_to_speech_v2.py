import tempfile
import PyPDF2
from gtts import gTTS
from pygame import mixer
import io
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    pdf_text = ""

    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    return pdf_text

def tts(file_path, speed=1.0):
    with open(file_path, 'rb') as file:
        pdf_text = extract_text_from_pdf(file)

    tts = gTTS(text=pdf_text, lang='en', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(1.0)
    mixer.music.load(fp)
    mixer.music.play()

    while mixer.music.get_busy():
        user_input = input("Enter 'p' to pause, 'r' to resume, 'f' to fast forward, or 'q' to quit: ")
        if user_input == 'p':
            mixer.music.pause()
        elif user_input == 'r':
            mixer.music.unpause()
        elif user_input == 'f':
            speed = float(input("Enter a speed multiplier (e.g. 2.0 for double speed): "))
            mixer.music.set_volume(speed)
        elif user_input == 'q':
            mixer.music.stop()
            break
    mixer.quit()

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
    tts(file_path)



'''
import tempfile
from gtts import gTTS
from pygame import mixer
import io
from io import BytesIO

def tts(file_path, speed=1.0):
    with open(file_path, 'rb') as file:
        text = file.read()

    tts = gTTS(text=text, lang='en', slow=False)
    #fp = tempfile.TemporaryFile()
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(1.0)
    mixer.music.load(fp)
    mixer.music.play()

    while mixer.music.get_busy():
        user_input = input("Enter 'p' to pause, 'r' to resume, 'f' to fast forward, or 'q' to quit: ")
        if user_input == 'p':
            mixer.music.pause()
        elif user_input == 'r':
            mixer.music.unpause()
        elif user_input == 'f':
            speed = float(input("Enter a speed multiplier (e.g. 2.0 for double speed): "))
            mixer.music.set_volume(speed)
        elif user_input == 'q':
            mixer.music.stop()
            break

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/LockhartsLament.pdf'
    tts(file_path)


from gtts import gTTS
import os
import io
from pygame import mixer
from io import BytesIO


def tts(file_path, speed=1.0):
    with open(file_path, 'r', encoding="utf8") as file:
        text = file.read()

    tts = gTTS(text=text, lang='en', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(1.0)
    mixer.music.load(fp)
    mixer.music.play()

    while mixer.music.get_busy():
        user_input = input("Enter 'p' to pause, 'r' to resume, 'f' to fast forward, or 'q' to quit: ")
        if user_input == 'p':
            mixer.music.pause()
        elif user_input == 'r':
            mixer.music.unpause()
        elif user_input == 'f':
            speed = float(input("Enter a speed multiplier (e.g. 2.0 for double speed): "))
            mixer.music.set_volume(speed)
        elif user_input == 'q':
            mixer.music.stop()
            break

def tts(file_path, speed=1.0):
    with open(file_path, 'rb') as file:
        content = file.read()

    try:
        text = content.decode("utf-8")
    except:
        text = content.decode("ISO-8859-1")

    tts = gTTS(text=text, lang='en', slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(1.0)
    mixer.music.load(fp)
    mixer.music.play()

    while mixer.music.get_busy():
        user_input = input("Enter 'p' to pause, 'r' to resume, 'f' to fast forward, or 'q' to quit: ")
        if user_input == 'p':
            mixer.music.pause()
        elif user_input == 'r':
            mixer.music.unpause()
        elif user_input == 'f':
            speed = float(input("Enter a speed multiplier (e.g. 2.0 for double speed): "))
            mixer.music.set_volume(speed)
        elif user_input == 'q':
            mixer.music.stop()
            break

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/LockhartsLament.pdf'
    tts(file_path)

from gtts import gTTS
from io import BytesIO
from pygame import mixer

def tts(file_path, speed=1.0):
    with open(file_path, 'rb') as file:
        text = file.read()

    tts = gTTS(text=text, lang='en', slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(1.0)
    mixer.music.load(fp)
    mixer.music.play()

    while mixer.music.get_busy():
        user_input = input("Enter 'p' to pause, 'r' to resume, 'f' to fast forward, or 'q' to quit: ")
        if user_input == 'p':
            mixer.music.pause()
        elif user_input == 'r':
            mixer.music.unpause()
        elif user_input == 'f':
            speed = float(input("Enter a speed multiplier (e.g. 2.0 for double speed): "))
            mixer.music.set_volume(speed)
        elif user_input == 'q':
            mixer.music.stop()
            break

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/LockhartsLament.pdf'
    tts(file_path)
'''
