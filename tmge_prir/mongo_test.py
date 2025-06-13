from pymongo import MongoClient
import certifi

uri = "mongodb+srv://trotsenkoyana7:Yana200676@baza5a.sytm3y5.mongodb.net/?retryWrites=true&w=majority&appName=Baza5a"

client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

try:
    print(client.server_info())  # Testuje połączenie
    print("Połączono z MongoDB Atlas!")
except Exception as e:
    print("Błąd połączenia:", e)
