import requests

API_TOKEN = "AQUÍ_TU_TOKEN"  # Debes poner tu token real
VIDEO_ID = "jNQXAC9IVRw"

url = "https://www.youtube-transcript.io/api/transcripts"

headers = {
    "Authorization": f"Basic {API_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "ids": [VIDEO_ID]
}

response = requests.post(url, headers=headers, json=payload)

print("Código:", response.status_code)
print("Respuesta:")
print(response.json())
