# 🕷 Web Crawler Distributed Application

Projekt aplikacji rozproszonej do selektywnego pobierania danych z witryn internetowych według zadanych profili. Zrealizowano z wykorzystaniem technologii: Python, Flask, MongoDB, multiprocessing, asyncio oraz Docker.

## 📌 Opis projektu

Aplikacja pobiera, przetwarza i zapisuje dane zgodne z ustalonym profilem danych. Całość została podzielona na 3 moduły:

- **Interfejs użytkownika (Flask)**
- **Silnik przetwarzający (multiprocessing + asyncio)**
- **Baza danych (MongoDB)**

## 📁 Struktura danych

Pobrane dane dzielą się na 4 główne grupy:
1. Adresy e-mail
2. Adresy korespondencyjne
3. Schematy organizacyjne (struktura firm, nazwiska)
4. Linki zewnętrzne i zasoby (np. do dokumentów PDF, DOCX)

## ⚙️ Technologie

- Python 3.10
- Flask
- BeautifulSoup4
- asyncio + multiprocessing
- MongoDB (zdalna lub lokalna w Dockerze)
- Docker + Docker Compose

## 🧠 Architektura

tmge_prir/
│
├── gui/                         # Moduł interfejsu użytkownika (Flask)
│   ├── app.py                   # Główna aplikacja Flask – serwuje dane z MongoDB
│   ├── templates/               # Szablony HTML (index.html, band_detail.html, 404.html)
│   ├── static/                  # Pliki statyczne
│   │   ├── img/                 # Zdjęcia zespołów
│   │   │   ├── Band_Maid.jpg
│   │   │   ├── Buck_Tick.jpg
│   │   │   └── ...
│   │   └── style.css            # Stylizacja aplikacji webowej (ciemny, rockowy klimat)
│   ├── requirements.txt         # Wymagane biblioteki dla GUI
│   └── Dockerfile               # Obraz Dockera dla interfejsu Flask
│
├── scraper/                     # Silnik scrapujący dane (asynchroniczny + multiprocessing)
│   ├── scraper.py               # Główna logika scrapera (asyncio, multiprocessing)
│   ├── mongo_test.py            # Testowe połączenie z bazą MongoDB
│   ├── requirements.txt         # Wymagane biblioteki (BeautifulSoup, aiohttp, pymongo, itd.)
│   └── Dockerfile               # Obraz Dockera dla scrapera
│
├── docker-compose.yml           # Kompozycja Dockera – uruchamia GUI, scraper i MongoDB
│
└── README.md                    # Opis projektu, instalacji i uruchomienia



### 📦 Moduły Dockera

- `frontend`: Serwer Flask (interfejs użytkownika)
- `crawler`: Główny silnik przetwarzający dane
- `mongodb`: Baza danych z danymi wejściowymi i wynikami

## 🚀 Uruchomienie

```bash
git clone https://github.com/yunayana/tmge_prir.git
cd tmge_prir
docker-compose up --build

