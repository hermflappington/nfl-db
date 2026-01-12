import duckdb
from pathlib import Path
import re

# 📁 Folder on your Desktop where Parquet files are
parquet_dir = Path(r"C:\Users\leste\Desktop\BOOK_OUTPUT")

# 🦆 Your DuckDB file
db_path = Path("db/nfl.duckdb")
db_path.parent.mkdir(parents=True, exist_ok=True)

# Connect to DuckDB
con = duckdb.connect(str(db_path))

# Scan all .parquet files
parquet_files = list(parquet_dir.glob("*.parquet"))

if not parquet_files:
    print("❌ No .parquet files found in:", parquet_dir)
    exit()

for file in parquet_files:
    # Clean view name: lowercase, replace spaces/punctuation with underscore
    view_name = re.sub(r"[^a-zA-Z0-9]", "_", file.stem).lower()

    # Register view
    con.execute(f"""
        CREATE OR REPLACE VIEW {view_name} AS
        SELECT * FROM '{file}'
    """)
    print(f"✅ Registered view: {view_name}")

print("🟢 All .parquet files registered in DuckDB.")
