import os
import requests
from dotenv import load_dotenv

load_dotenv()

def consultar_indicador(codigo):
    base = os.getenv("API_BASE_URL")
    r = requests.get(f"{base}/{codigo}", timeout=10)
    r.raise_for_status()
    return r.json()
