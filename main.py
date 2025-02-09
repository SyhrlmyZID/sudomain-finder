import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def normalize_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url

def find_urls(base_url):
    try:
        base_url = normalize_url(base_url)
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        urls = set()
        for link in soup.find_all('a', href=True):
            
            full_url = urljoin(base_url, link['href'])
            if base_url.split("//")[-1] in full_url:
                urls.add(full_url)
        
        print(f"\n[HASIL SCANNING] {len(urls)} URL ditemukan:")
        for i, url in enumerate(urls, 1):
            print(f"{i}. {url}")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    base_url = input("Masukan url website (contoh: google.com): ")
    print("Tunggu sebentar...\n")
    find_urls(base_url)
