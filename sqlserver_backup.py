import pymssql
import time

from settings import *

conn = pymssql.connect(server=SERVER_HOST, user=USERNAME, password=PASSWORD)
conn.autocommit(True)
cursor = conn.cursor()

is_first = True

for db in DATABASES:
    if not is_first:
        time.sleep(PAUSE)
    is_first = False

    file_names = ""
    for i in range(1,FILE_PARTS+1):
        file_names += f"URL='{STORE_URL}{db}-part{i}.bak'" + (", " if i!=FILE_PARTS else "")
    sql = f"BACKUP DATABASE {db} TO {file_names} WITH FORMAT, MAXTRANSFERSIZE=20971520;"
    print(f"Executing : {sql} ...")
    cursor.execute(sql)



conn.close()