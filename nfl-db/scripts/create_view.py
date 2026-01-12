import duckdb

# Connect to the database
con = duckdb.connect("db/nfl.duckdb")

# Create or replace the cleaned-up coaches view
con.execute("""
    CREATE OR REPLACE VIEW canon_coaches AS
    SELECT
        year,
        team,
        TRIM(coach) AS coach_name,
        TRIM(role) AS role
    FROM master_coaching_long_corrected_3
    WHERE coach IS NOT NULL;
""")

print("✅ View 'canon_coaches' created.")
