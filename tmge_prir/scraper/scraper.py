import asyncio
import aiohttp
from bs4 import BeautifulSoup
from pymongo import MongoClient
import logging
from urllib.parse import urlparse
import certifi

# MongoDB
client = MongoClient(
    "mongodb+srv://trotsenkoyana7:Yana200676@baza5a.sytm3y5.mongodb.net/?retryWrites=true&w=majority&appName=Baza5a",
    tls=True,
    tlsCAFile=certifi.where()
)
db = client['music_scraper']
coll = db['jrock_bands']

# Logging
logging.basicConfig(level=logging.INFO)

# Headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )
}

WIKI_URLS = [
    "https://en.wikipedia.org/wiki/Buck-Tick",
    "https://en.wikipedia.org/wiki/Babymetal",
    "https://en.wikipedia.org/wiki/Church_of_Misery",
    "https://en.wikipedia.org/wiki/Asian_Kung-Fu_Generation",
    "https://en.wikipedia.org/wiki/Acid_Black_Cherry",
    "https://en.wikipedia.org/wiki/Acid_Android",
    "https://en.wikipedia.org/wiki/Band-Maid",
    "https://en.wikipedia.org/wiki/Czecho_No_Republic",
]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return await response.text()
            logging.error(f"Błąd {response.status} dla {url}")
    except Exception as e:
        logging.error(f"Błąd pobierania {url}: {e}")
    return ""

async def parse_band(session, url):
    html = await fetch(session, url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').text.strip()
    lead = soup.find('p')
    summary = lead.text.strip() if lead else "Brak opisu"

    infobox = soup.find('table', {'class': 'infobox'})
    genre, origin, years_active = "Nieznane", "Nieznane", "Nieznane"

    if infobox:
        for row in infobox.find_all('tr'):
            header = row.find('th')
            data = row.find('td')
            if not header or not data:
                continue
            key = header.text.strip().lower()
            if 'genre' in key:
                genre = data.text.strip()
            elif 'origin' in key:
                origin = data.text.strip()
            elif 'years active' in key:
                years_active = data.text.strip()

    band = {
        'name': title,
        'summary': summary,
        'genre': genre,
        'origin': origin,
        'years_active': years_active,
        'url': url
    }

    coll.update_one({'url': url}, {'$set': band}, upsert=True)
    logging.info(f"Zapisano zespół: {title}")

async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = [parse_band(session, url) for url in WIKI_URLS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
