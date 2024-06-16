import pandas as pd
import psycopg2
from psycopg2 import sql
from datetime import datetime
def read_logs(file_path):
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                ip = parts[0]
                date_str = parts[3][1:] + ' ' + parts[4][:-1]
                date = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
                request = ' '.join(parts[5:8])
                if parts[8] == '"-"':
                    status = None
                else:
                    status = int(parts[8])
                if parts[9] == '"-"':
                    size = None
                else:
                    size = int(parts[9])
                logs.append((ip, date, request, status, size))
    return logs
def write_to_db(logs):
    conn = psycopg2.connect(
        dbname="save",
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()
    insert_query = sql.SQL("""
        INSERT INTO access_logs (ip, date, request, status, size)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (ip, date, request) DO NOTHING
    """)
    for log in logs:
        cur.execute(insert_query, log)
    conn.commit()
    cur.close()
    conn.close()
def llog():
    file_path = 'access.log'
    logs = read_logs(file_path)
    write_to_db(logs)
if __name__ == "__main__":
    llog()