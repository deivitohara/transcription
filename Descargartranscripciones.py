# descargar_transcripciones.py
from youtube_transcript_api import YouTubeTranscriptApi
from obtener_links import obtener_links_playlist
from urllib.parse import urlparse, parse_qs
import os

def extraer_id(url):
    return parse_qs(urlparse(url).query).get("v", [""])[0]

def guardar_transcripcion(video_id, transcript):
    nombre_archivo = f"{video_id}.txt"
    #nombre_archivo = os.path.join("lista", f"{video_id}.txt")
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for snippet in transcript:
            f.write(snippet.text + "\n")
    print(f"Transcripción guardada en {nombre_archivo}")

def procesar_playlist(url_playlist=None):
    ytt_api = YouTubeTranscriptApi()

    print("Obteniendo enlaces de la playlist...")
    links = obtener_links_playlist(url_playlist)

    print(f"Se han encontrado {len(links)} vídeos.\n")

    for link in links:
        video_id = extraer_id(link)
        print(f"Procesando vídeo: {video_id}")

        try:
            transcript = ytt_api.fetch(video_id, languages=['es'])
            guardar_transcripcion(video_id, transcript)
        except Exception as e:
            print(f"No se pudo obtener la transcripción de {video_id}: {e}")

if __name__ == "__main__":
    # Si no pasas nada, usa la playlist por defecto
    procesar_playlist()