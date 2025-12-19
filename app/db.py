import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    dsn = f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_SERVICE')}"
    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=dsn
    )
