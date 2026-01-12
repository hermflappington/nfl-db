import pandas as pd
from pathlib import Path

source = Path("C:/Users/leste/Desktop/BOOK_OUTPUT")
files = list(source.glob("*.parquet"))

# include broader set of keywords
kw = ["award", "mvp", "dpoy", "opoy", "coty", "eoty", "coach"]

award_files = [f for f in files if any(k in f.name.lower() for k in kw)]

dfs = [pd.read_parquet(f) for f in award_files]
merged = pd.concat(dfs, ignore_index=True)

out = source / "merged_all_awards.parquet"
merged.to_parquet(out)

print(f"✅ merged {len(award_files)} award files into {out.name}")