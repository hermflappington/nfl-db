import duckdb

# Connect to your DuckDB
con = duckdb.connect("db/nfl.duckdb")

# List all views
views = con.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'main' AND table_type = 'VIEW'
""").fetchall()

print("🗂️ Found views:", len(views))
print("-" * 40)

# Preview columns from each view
for (view,) in views:
    print(f"🔹 {view}")
    try:
        columns = con.execute(f"PRAGMA table_info({view})").fetchall()
        for col in columns[:5]:  # Show only first 5 columns
            print(f"   - {col[1]} ({col[2]})")
    except Exception as e:
        print(f"   ⚠️ Error reading {view}: {e}")
    print("-" * 40)
