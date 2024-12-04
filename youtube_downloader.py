import os
import yt_dlp
from pydub import AudioSegment

if not os.path.exists("songs"):
    os.makedirs("songs")

def download_videos_from_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'songs/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_audio_from_videos():
    for video_file in os.listdir('songs'):
        if video_file.endswith(('.mp4', '.mkv', '.webm', '.avi')):
            video_path = os.path.join('songs', video_file)
            audio = AudioSegment.from_file(video_path)
            audio_file_path = os.path.join('songs', f"{os.path.splitext(video_file)[0]}.mp3")
            audio.export(audio_file_path, format="mp3")
            os.remove(video_path)
            print(f"Áudio extraído e vídeo {video_file} apagado.")

playlist_url = input("Digite a URL da playlist: ")

download_videos_from_playlist(playlist_url)
extract_audio_from_videos()
