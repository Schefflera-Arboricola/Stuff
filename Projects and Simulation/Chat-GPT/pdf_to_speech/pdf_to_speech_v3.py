import pygame
import pyttsx3
from PyPDF2 import PdfReader

# initialize pygame mixer
pygame.init()
pygame.display.set_mode()

# initialize tts engine
engine = pyttsx3.init()

# function to extract text from pdf
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

# function to convert pdf to speech
def pdf_to_speech(file_path):
    pdf_text = extract_text_from_pdf(file_path)
    engine.say(pdf_text)
    engine.runAndWait()

# function to pause speech
def pause_speech():
    engine.pause()

# function to resume speech
def resume_speech():
    engine.resume()

# function to fast forward speech
def fast_forward_speech(speed):
    engine.setProperty('rate', speed)


def speak_text(text, speed=175):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()
    
# read pdf file
file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
pdf_to_speech(file_path)

# set up pygame window
screen = pygame.display.set_mode((400, 300))
#print(screen)
pygame.display.set_caption("PDF to speech with Pygame")

# wait for events in the pygame window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause_speech()
            elif event.key == pygame.K_RETURN:
                resume_speech()
            elif event.key == pygame.K_UP:
                fast_forward_speech(200)
            elif event.key == pygame.K_DOWN:
                fast_forward_speech(100)

# quit pygame
pygame.quit()


'''

import PyPDF2
import pyttsx3
import time

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    pdf_text = ''
    for page in range(pdf_reader.getNumPages()):
        pdf_text += pdf_reader.getPage(page).extract_text()
    return pdf_text


def speak_text(text, speed=175):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()

def tts(file_path):
    with open(file_path, 'rb') as file:
        pdf_text = extract_text_from_pdf(file)
    speak_text(pdf_text)

def fast_forward(speed=250):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)

def pause():
    engine = pyttsx3.init()
    engine.pause()

def resume():
    engine = pyttsx3.init()
    engine.resume()

file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
tts(file_path)



import PyPDF2
import threading
import pygame

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    pdf_text = ''
    for page in range(pdf_reader.numPages):
        pdf_text += pdf_reader.getPage(page).extractText()
    return pdf_text

def speak_text(text, speed):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(text)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    clock.tick(speed)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(speed)

def tts(file_path):
    with open(file_path, 'rb') as file:
        pdf_text = extract_text_from_pdf(file)
        tts_thread = threading.Thread(target=speak_text, args=(pdf_text, 10))
        tts_thread.start()

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
    tts(file_path)

import tempfile
import PyPDF2
from gtts import gTTS
from pygame import mixer
import io
import threading

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    pdf_text = ""

    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    return pdf_text

def tts_thread(pdf_text, speed=1.0):
    tts = gTTS(text=pdf_text, lang='en', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(speed)
    mixer.music.load(fp)
    mixer.music.play()

def tts(file_path, speed=1.0):
    with open(file_path, 'rb') as file:
        pdf_text = extract_text_from_pdf(file)

    tts_thread = threading.Thread(target=speak_text, args=(pdf_text, speed))
    tts_thread.start()

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
    file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
    tts(file_path)


import tempfile
import PyPDF2
from gtts import gTTS
from pygame import mixer
import io
import threading
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
    return pdf_text

def tts_thread(pdf_text, speed=1.0):
    tts = gTTS(text=pdf_text, lang='en', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    mixer.init()
    mixer.music.set_volume(speed)
    mixer.music.load(fp)
    mixer.music.play()

def tts(file_path, speed=1.0):
    tts_thread = threading.Thread(target=tts_thread, args=(pdf_text, speed))
    pdf_text = extract_text_from_pdf(file_path)
    tts_thread.start()

if __name__ == '__main__':
    file_path = '/Users/aditi/Desktop/book/Why I am an Atheist_text.pdf'
    tts(file_path)
'''
