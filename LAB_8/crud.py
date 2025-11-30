import pandas as pd

def insert_incident(conn, date, incident_type, severity, status, description, reported_by=None):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO cyber_incidents (date, incident_type, severity, status, description, reported_by)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (date, incident_type, severity, status, description, reported_by))
    conn.commit()

def get_all_incidents(conn):
    return pd.read_sql_query("SELECT * FROM cyber_incidents", conn)

def update_incident_status(conn, incident_id, new_status):
    cur = conn.cursor()
    cur.execute("UPDATE cyber_incidents SET status=? WHERE id=?", (new_status, incident_id))
    conn.commit()

def delete_incident(conn, incident_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM cyber_incidents WHERE id=?", (incident_id,))
    conn.commit()