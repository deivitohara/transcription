from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
video_id = "bsqLYAg-brU"
fetched_transcript=ytt_api.fetch(video_id, languages=['es'])

# is iterable
for snippet in fetched_transcript:
    print(snippet.text)

#url_video = "https://www.youtube.com/watch?v=bsqLYAg-brU&list=PLp2uuQBLuFrnx3UIB1M6cE8VOzpG8udRN&index=1&pp=iAQB"
