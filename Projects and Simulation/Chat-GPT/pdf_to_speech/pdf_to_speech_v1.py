import PyPDF2
import pyttsx3

def pdf_to_speech(file_path):
    pdf_reader = PyPDF2.PdfReader(file_path)
    num_pages = len(pdf_reader.pages)
    text = ""
    for i in range(num_pages):
        text += pdf_reader.pages[i].extract_text()
    
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
    engine.say(text)
    engine.runAndWait()

file_path = '/Users/aditi/Desktop/book/LockhartsLament.pdf'
pdf_to_speech(file_path)
