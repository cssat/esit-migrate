import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

connections = { 
        'ESIT_COPY': pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=delolydb12021;'
                      'DATABASE=ESITDMS_COPY;'
                      f"UID={os.getenv('ESIT_COPY_USER')};"
                      f"PWD={os.getenv('ESIT_COPY_PASSWORD')}")
}

def get_connection(dbname):
    return connections[dbname]
