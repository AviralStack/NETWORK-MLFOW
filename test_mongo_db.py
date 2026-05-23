from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi  # 1. Import certifi
from dotenv import load_dotenv
import os

mongo_env = load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

url = MONGO_DB_URL

# 2. Add tlsCAFile=certifi.where() to your MongoClient
client = MongoClient(
    url, 
    server_api=ServerApi('1'),
    tlsCAFile=certifi.where()
)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)