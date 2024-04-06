# audio_extractor - v3
# script to extract and download audio of a youtube video given its url

from pytube import YouTube


def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Input output directory:")

    download_audio(video_url, output_directory)
