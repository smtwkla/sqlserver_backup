import pymssql
import time

from settings import *

conn = pymssql.connect(server=SERVER_HOST, user=USERNAME, password=PASSWORD)
conn.autocommit(True)
cursor = conn.cursor()


for db in DATABASES:
    file_names = ""
    for i in range(1,FILE_PARTS+1):
        file_names += f"URL='{STORE_URL}{db}-part{i}.bak'" + (", " if i!=FILE_PARTS else "")
    sql = f"BACKUP DATABASE {db} TO {file_names} WITH FORMAT, MAXTRANSFERSIZE=20971520;"
    print(f"Executing : {sql} ...")
    cursor.execute(sql)
    time.sleep(PAUSE)


conn.close()