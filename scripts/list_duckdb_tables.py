import duckdb

# Connect to the database
con = duckdb.connect("db/nfl.duckdb")

# Get all base tables (not views)
tables = con.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'main'
      AND table_type = 'BASE TABLE'
""").fetchall()

print("📦 Tables found:", len(tables))

for t in tables:
    table_name = t[0]
    count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"🧮 {table_name}: {count} rows")

con.close()
