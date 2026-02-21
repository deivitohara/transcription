import yt_dlp

url = "https://www.youtube.com/watch?v=GAh6owu-UnU"

ydl_opts = {
    "skip_download": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["es"],
    "subtitlesformat": "srt"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
