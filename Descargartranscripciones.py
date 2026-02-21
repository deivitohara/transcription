from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        return parse_qs(query.query).get('v', [None])[0]
    return None

def descargar_transcripcion(url, archivo_salida="transcripcion.txt"):
    video_id = get_video_id(url)
    if not video_id:
        print("No se pudo extraer el ID del vídeo.")
        return

    try:
        # Usamos el método que tu instalación SÍ tiene
        transcripts, _ = YouTubeTranscriptApi.get_transcripts([video_id], languages=['es', 'en'])
        transcript = transcripts[video_id]

        with open(archivo_salida, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(entry['text'] + "\n")

        print(f"Transcripción guardada en: {archivo_salida}")

    except Exception as e:
        print("Error al obtener la transcripción:", e)


# Ejemplo de uso
url_video = "https://www.youtube.com/watch?v=bsqLYAg-brU&list=PLp2uuQBLuFrnx3UIB1M6cE8VOzpG8udRN&index=1&pp=iAQB"
descargar_transcripcion(url_video)