import duckdb

con = duckdb.connect("db/nfl.duckdb")
tables = con.execute("SHOW TABLES").fetchall()

print("📋 Tables found:")
for table in tables:
    print("-", table[0])