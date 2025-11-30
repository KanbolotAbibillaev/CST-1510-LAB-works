from database import *
from crud import *
from analytics import *

conn = connect_database()

create_cyber_incidents_table(conn)
create_it_tickets_table(conn)
create_datasets_metadata_table(conn)

insert_incident(conn, "2025-11-30", "Phishing", "High", "Open", "Fake login", "admin")

print(get_all_incidents(conn))

update_incident_status(conn, 1, "Closed")
print(get_all_incidents(conn))

print(get_high_severity_by_status(conn))

delete_incident(conn, 1)
print(get_all_incidents(conn))

conn.close()