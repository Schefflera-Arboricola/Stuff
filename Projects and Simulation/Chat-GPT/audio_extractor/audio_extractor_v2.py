#ChatGPT Jan 30 Version. Free Research Preview

import youtube_dl
import os
from pydub import AudioSegment

def download_audio(video_link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_link, download=True)
        filename = info_dict.get("title", "") + ".mp3"
        filename = filename.replace("/", "-")
        sound = AudioSegment.from_file(filename, format="mp3")

video_link = "https://youtu.be/7maJOI3QMu0"
download_audio(video_link)

'''

from pydub import AudioSegment
import youtube_dl

def download_audio(video_link):
    # download the audio using youtube-dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])

    # load the downloaded audio file
    filename = ydl.prepare_filename(video_link).split("/")[-1].split(".")[0] + ".mp3"
    sound = AudioSegment.from_file(filename, format="mp3")

    # save the audio to a new file
    new_filename = "converted_" + filename
    sound.export(new_filename, format="mp3")

video_link = 'https://youtu.be/OzDRZbsMa_4'
download_audio(video_link)
'''
