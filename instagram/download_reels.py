import instaloader
import re
import os

# Funktion zum Extrahieren der Shortcode aus einem Instagram-Link
def get_shortcode(url):
    pattern = r"(?:/reel/|/p/)([A-Za-z0-9_-]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# Funktion zum Lesen der Links aus der .txt-Datei
def read_links_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Datei {file_path} nicht gefunden!")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        links = [line.strip() for line in file if line.strip()]
    return links

# Hauptfunktion zum Herunterladen der Reels
def download_reels(txt_file_path, download_dir="reels"):
    # Instaloader initialisieren
    L = instaloader.Instaloader(download_pictures=False, download_videos=True, download_comments=False, download_geotags=False, download_video_thumbnails=False)

    # Download-Verzeichnis erstellen, falls es nicht existiert
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Links aus der Datei lesen
    links = read_links_from_file(txt_file_path)
    if not links:
        print("Keine Links in der Datei gefunden.")
        return

    # Jeden Link verarbeiten
    for url in links:
        shortcode = get_shortcode(url)
        if shortcode:
            try:
                print(f"Lade Reel herunter: {url}")
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                L.download_post(post, target=download_dir)
                print(f"Reel {shortcode} erfolgreich heruntergeladen.")
            except Exception as e:
                print(f"Fehler beim Herunterladen von {url}: {str(e)}")
        else:
            print(f"Ungültiger Link: {url}")

# Beispielaufruf
if __name__ == "__main__":
    txt_file = "reels.txt"
    download_dir = "downloaded_reels"
    download_reels(txt_file, download_dir)