import psycopg2
from datetime import datetime
def fetch_logs(group_by=None, date_range=None):
    conn = psycopg2.connect(
        dbname="save",
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()

    if group_by == 'ip':
        select_query = "SELECT ip, COUNT(*) FROM access_logs GROUP BY ip ORDER BY ip"
    elif group_by == 'date':
        select_query = "SELECT date_trunc('day', date) AS day, COUNT(*) FROM access_logs GROUP BY day ORDER BY day"
    elif date_range:
        start_date, end_date = date_range
        select_query = f"SELECT * FROM access_logs WHERE date BETWEEN '{start_date}' AND '{end_date}'"
    else:
        select_query = "SELECT * FROM access_logs"

    cur.execute(select_query)
    logs = cur.fetchall()
    cur.close()
    conn.close()

    return logs


def bd(group_by=None, date_range=None):
    logs = fetch_logs(group_by, date_range)
    return logs


if __name__ == "__main__":
    bd()