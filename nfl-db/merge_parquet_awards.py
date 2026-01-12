import pandas as pd
from pathlib import Path

# Set your source and output paths
source_dir = Path("C:/Users/leste/Desktop/BOOK_OUTPUT")
output_file = Path("data/merged_awards.parquet")

# Match only parquet files
parquet_files = list(source_dir.glob("*.parquet"))

# Filter for files likely related to awards
award_files = [f for f in parquet_files if "award" in f.name.lower()]

# Read and merge
dfs = [pd.read_parquet(file) for file in award_files]
merged_df = pd.concat(dfs, ignore_index=True)

# Ensure destination folder exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Save as merged file
merged_df.to_parquet(output_file)

print(f"✅ Merged {len(award_files)} files into {output_file}")