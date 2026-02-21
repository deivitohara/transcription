from pytube import Playlist
import os

def obtener_links_playlist(url_playlist: str = None) -> list:
    """
    Devuelve una lista con todos los enlaces de los vídeos de una playlist de YouTube
    y además los guarda en un archivo .txt.
    """

    if url_playlist is None:
        url_playlist = "https://youtube.com/playlist?list=PLp2uuQBLuFrnx3UIB1M6cE8VOzpG8udRN&si=FspnN2UOC9O11TbU"

    print("Cargando playlist...")

    playlist = Playlist(url_playlist)

    # Fix necesario porque pytube a veces no carga todos los vídeos
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

    links = list(playlist.video_urls)

    # Aviso si no ha cargado nada
    if not links:
        print("⚠️ No se han encontrado vídeos. Pytube no ha podido cargar la playlist.")
        return []

    # Nombre del archivo
    nombre_archivo = "links_playlist.txt"

    # Guardar los enlaces en el archivo
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")

    ruta = os.path.abspath(nombre_archivo)
    print(f"Archivo creado correctamente en:\n{ruta}")

    return links
if __name__ == "__main__":
    # Si no pasas nada, usa la playlist por defecto
    obtener_links_playlist()