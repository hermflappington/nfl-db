import nfl_data_py as nfl              # ✅ Official Python interface for NFLverse data
import duckdb                          # ✅ SQL engine for querying local files
import pandas as pd                    # ✅ Data handling
from pathlib import Path               # ✅ Cross-platform file path management

# — Step 1: Select the season —
SEASON = 2023
print(f"📥 Loading roster data for {SEASON} via nfl-data-py...")

# ✅ Correct function for roster data (was previously incorrect)
roster_df = nfl.import_seasonal_rosters([SEASON])

# — Step 2: Set up folders and filenames —
DATA_RAW = Path("data/raw")
DATA_PARQUET = Path("data/parquet")
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PARQUET.mkdir(parents=True, exist_ok=True)

csv_file = DATA_RAW / f"roster_{SEASON}.csv"
parquet_file = DATA_PARQUET / f"roster_{SEASON}.parquet"

# — Step 3: Save CSV and Parquet —
roster_df.to_csv(csv_file, index=False)
print(f"✅ Saved CSV to: {csv_file}")

roster_df.to_parquet(parquet_file, index=False)
print(f"✅ Saved Parquet to: {parquet_file}")

# — Step 4: Load into DuckDB as virtual view —
print("🦆 Connecting to DuckDB and creating virtual view...")

# ✅ Using in-memory DuckDB for now; can later change to: duckdb.connect("db/nfl.duckdb")
con = duckdb.connect()

# ✅ Creates a DuckDB view over the Parquet file (no data copy)
con.execute(f"""
    CREATE OR REPLACE VIEW roster_{SEASON} AS
    SELECT * FROM '{parquet_file}'
""")

print(f"✅ DuckDB view 'roster_{SEASON}' created.")

# — Step 5: Run a basic query —
print("🔍 Sample query: number of players per team")

query = f"""
    SELECT team, COUNT(*) AS players
    FROM roster_{SEASON}
    GROUP BY team
    ORDER BY players DESC
"""

result = con.execute(query).fetchdf()
print(result)

