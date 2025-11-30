import pandas as pd

def get_high_severity_by_status(conn):
    q = """
    SELECT status, COUNT(*) AS count
    FROM cyber_incidents
    WHERE severity='High'
    GROUP BY status
    ORDER BY count DESC
    """
    return pd.read_sql_query(q, conn)

def get_incident_types_with_many_cases(conn, min_count=5):
    q = """
    SELECT incident_type, COUNT(*) AS count
    FROM cyber_incidents
    GROUP BY incident_type
    HAVING COUNT(*) >= ?
    ORDER BY count DESC
    """
    return pd.read_sql_query(q, conn, params=(min_count,))