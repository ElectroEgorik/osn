import json
import psycopg2
from datetime import datetime
def fetch_logs():
    conn = psycopg2.connect(
        dbname="save",
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()
    select_query = "SELECT * FROM access_logs"
    cur.execute(select_query)
    logs = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    logs_dict = [dict(zip(column_names, log)) for log in logs]

    return logs_dict

def json_serial(obj):
    """Сериализация объектов datetime в формат ISO 8601."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")
def write_logs_to_json(logs, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(logs, json_file, indent=4, default=json_serial)
def js():
    logs = fetch_logs()
    file_path = 'access_logs.json'
    write_logs_to_json(logs, file_path)
    print(f"Данные успешно записаны в файл {file_path}")

if __name__ == "__main__":
    js()

