from pytube import Playlist

def obtener_links_playlist(url_playlist: str) -> list:
    """
    Devuelve una lista con todos los enlaces de los vídeos de una playlist de YouTube.
    """
    if url_playlist is None:
        url_playlist = "https://youtube.com/playlist?list=PLp2uuQBLuFrnx3UIB1M6cE8VOzpG8udRN&si=FspnN2UOC9O11TbU"


    playlist = Playlist(url_playlist)

    # Fix necesario porque pytube a veces no carga todos los vídeos
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

    return list(playlist.video_urls)
