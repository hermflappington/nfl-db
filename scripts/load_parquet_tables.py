import duckdb
from pathlib import Path
import re

# Folder with your parquet files
PARQUET_DIR = Path(r"C:\Users\leste\Desktop\BOOK_OUTPUT")

# DuckDB database file
DB_PATH = Path("db/nfl.duckdb")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Connect to DuckDB
con = duckdb.connect(DB_PATH)

parquet_files = list(PARQUET_DIR.glob("*.parquet"))

if not parquet_files:
    print("❌ No parquet files found.")
    exit()

for file in parquet_files:
    table_name = re.sub(r"[^a-zA-Z0-9]", "_", file.stem).lower()

    print(f"📥 Loading {file.name} → table `{table_name}`")

    con.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT * FROM read_parquet('{file}');
    """)

print("✅ ALL parquet files loaded as DuckDB TABLES.")
con.close()
