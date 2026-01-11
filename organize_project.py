import os
from pathlib import Path
import shutil

# Define folders
BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"
SCRIPTS_DIR = BASE_DIR / "scripts"

# Create folders if missing
for folder in [DATA_DIR, DB_DIR, SCRIPTS_DIR]:
    folder.mkdir(exist_ok=True)

# Move files by type or name
for file in BASE_DIR.glob("*"):
    if file.is_file():
        if file.suffix == ".py" and file.name != "organize_project.py":
            shutil.move(str(file), SCRIPTS_DIR / file.name)
        elif file.suffix == ".duckdb":
            shutil.move(str(file), DB_DIR / file.name)
        elif file.suffix in [".csv", ".xlsx"]:
            shutil.move(str(file), DATA_DIR / file.name)

# Create .gitignore
gitignore = BASE_DIR / ".gitignore"
if not gitignore.exists():
    gitignore.write_text("db/\ndata/\n")

print("✅ Project organized.")