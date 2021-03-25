import connection
import sys
import time

conn = connection.get_connection('ESIT_COPY')

cursor = conn.cursor()

for line in sys.stdin:
   print(line)
   time.sleep(1)