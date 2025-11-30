import pandas as pd
from pathlib import Path

def load_csv_to_table(conn, csv_path, table_name):
    path = Path(csv_path)
    if not path.exists():
        print("CSV not found:", path)
        return
    df = pd.read_csv(path)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"{len(df)} rows added to {table_name}")