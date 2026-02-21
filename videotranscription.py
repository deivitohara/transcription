from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# Extrae el ID de un vídeo a partir de su URL
def extraer_id(url):
    return parse_qs(urlparse(url).query).get("v", [""])[0]

# Guarda la transcripción en un archivo .txt
def guardar_transcripcion(video_id, transcript):
    nombre_archivo = f"{video_id}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for snippet in transcript:
            f.write(snippet.text + "\n")
    print(f"Transcripción guardada en {nombre_archivo}")

# Descarga la transcripción de un solo vídeo
def descargar_video(url_video=None):
    
    ytt_api = YouTubeTranscriptApi()

    if url_video is None:
        url_video = "https://www.youtube.com/watch?v=-NOy267DRJc"
    video_id = extraer_id(url_video)
    print(f"Procesando vídeo: {video_id}")

    # Intentos: español → inglés → cualquier idioma
    try:
        transcript = ytt_api.fetch(video_id, languages=['es'])
    except:
        try:
            transcript = ytt_api.fetch(video_id, languages=['en'])
        except:
            try:
                transcript = ytt_api.fetch(video_id)
            except Exception as e:
                print(f"No se pudo obtener la transcripción de {video_id}: {e}")
                return

    guardar_transcripcion(video_id, transcript)

# Ejecución
if __name__ == "__main__":
    
    descargar_video()