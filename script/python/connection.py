import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=delolydb12021;'
                      'DATABASE=ESITDMS_COPY;'
                      f"UID={os.getenv('DB_USER')};"
                      f"PWD={os.getenv('DB_PASSWORD')}")