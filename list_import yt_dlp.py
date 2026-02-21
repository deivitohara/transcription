import yt_dlp
import time
import random

# Archivo con las URLs (una por línea)
LISTA = "links_playlist.txt"

# Configuración de yt-dlp
ydl_opts = {
    "skip_download": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["es", "en"],  # idiomas permitidos
    "subtitlesformat": "srt",
    "quiet": False,
}

def procesar_video(url):
    print(f"\nProcesando: {url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✔ Subtítulos descargados")
    except Exception as e:
        print(f"❌ Error en {url}: {e}")

def main():
    with open(LISTA, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    for i, url in enumerate(urls, start=1):
        procesar_video(url)

        # Pausa aleatoria entre vídeos (1–3 segundos)
        espera = random.uniform(1, 3)
        print(f"Esperando {espera:.1f} segundos...\n")
        time.sleep(espera)

    print("\nProceso completado.")

if __name__ == "__main__":
    main()