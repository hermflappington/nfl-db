import requests
import duckdb
import pandas as pd
from pathlib import Path

# — Step 1: Set season —
SEASON = 2023

# — Step 2: Setup folders —
DATA_RAW = Path("data/raw")
DATA_PARQUET = Path("data/parquet")
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PARQUET.mkdir(parents=True, exist_ok=True)

# — Step 3: Download CSV —
ROSTER_URL = f"https://raw.githubusercontent.com/nflverse/nflverse-data/master/data/rosters/roster_{SEASON}.csv"
LOCAL_CSV = DATA_RAW / f"roster_{SEASON}.csv"
LOCAL_PARQUET = DATA_PARQUET / f"roster_{SEASON}.parquet"

print(f"📥 Downloading roster for {SEASON}...")
response = requests.get(ROSTER_URL)
response.raise_for_status()
with open(LOCAL_CSV, "wb") as f:
    f.write(response.content)
print(f"✅ Downloaded to {LOCAL_CSV}")

# — Step 4: Convert to Parquet —
print("🔄 Converting CSV to Parquet...")
df = pd.read_csv(LOCAL_CSV)
df.to_parquet(LOCAL_PARQUET, index=False)
print(f"✅ Saved Parquet: {LOCAL_PARQUET}")

# — Step 5: Query with DuckDB —
print("🦆 Connecting to DuckDB and creating virtual view...")
con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW roster_{SEASON} AS
    SELECT * FROM '{LOCAL_PARQUET}'
""")
print(f"✅ View 'roster_{SEASON}' created.")

# — Step 6: Sample query —
print("🔍 Sample query: players per team")
result = con.execute(f"""
    SELECT team, COUNT(*) AS players
    FROM roster_{SEASON}
    GROUP BY team
    ORDER BY players DESC
""").fetchdf()

print(result)
