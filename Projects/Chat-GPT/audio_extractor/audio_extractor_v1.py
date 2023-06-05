import youtube_dl
from pydub import AudioSegment

def download_audio(video_link):
    # Define options for youtube-dl
    ydl_opts = {
        # Select the best audio format available
        'format': 'bestaudio/best',
        # Use FFmpeg to extract audio from the video and convert it to MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Use youtube-dl to download the audio
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])

    # Use pydub to convert the audio to MP3
    # The input file is named after the video's id
    sound = AudioSegment.from_file(video_link.split("=")[-1] + ".mp3", format="mp3")
    # The output file is named "output.mp3"
    sound.export("output.mp3", format="mp3")

video_link='https://youtu.be/OzDRZbsMa_4'
download_audio(video_link)
