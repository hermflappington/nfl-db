import duckdb
import pandas as pd

# Load the CSV
df = pd.read_csv("USE_THIS_COACHING.csv")

# Connect to the database
con = duckdb.connect("db/nfl.duckdb")

# Optional: drop existing table to avoid conflicts
con.execute("DROP TABLE IF EXISTS main_coaching")

# Load DataFrame into DuckDB
con.execute("CREATE TABLE main_coaching AS SELECT * FROM df")

# Optional: confirm row count
row_count = con.execute("SELECT COUNT(*) FROM main_coaching").fetchone()[0]
print(f"✅ Loaded {row_count} rows into 'main_coaching' table.")

con.close()
