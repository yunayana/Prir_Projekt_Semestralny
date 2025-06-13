from flask import Flask, render_template, abort
from pymongo import MongoClient
import certifi

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://trotsenkoyana7:Yana200676@baza5a.sytm3y5.mongodb.net/?retryWrites=true&w=majority&appName=Baza5a",
    tls=True,
    tlsCAFile=certifi.where()
)

db = client['music_scraper']
coll = db['jrock_bands']

def add_image(band):
    images = {
        "Buck-Tick": "/static/img/Buck_Tick.jpg",
        "Babymetal": "/static/img/Baby_Metal.jpg",
        "Church of Misery": "/static/img/Church-of-Misery.jpg",
        "Asian Kung-Fu Generation": "/static/img/Asian_KungFu_Generation.jpg",
        "Acid Black Cherry": "/static/img/Acid_Black_Cherry.jpg",
        "Acid Android": "/static/img/Acid_Android.jpg",
        "Band-Maid": "/static/img/Band_Maid.jpg",
        "Czecho No Republic": "/static/img/Czecho_No_Republic.jpg",
    }
    band["image"] = images.get(band["name"], "/static/img/default.jpg")
    return band


@app.route("/")
def index():
    bands_raw = list(coll.find({}, {'_id': 0}))
    bands = [add_image(b) for b in bands_raw]
    return render_template("index.html", bands=bands)

@app.route("/band/<path:band_url>")
def band_detail(band_url):
    band_url = "https://" + band_url
    band = coll.find_one({'url': band_url}, {'_id': 0})
    if not band:
        abort(404)
    band = add_image(band)
    return render_template("band_detail.html", band=band)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
