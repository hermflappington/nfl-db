from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the merged awards file
df = pd.read_parquet("merged_all_awards.parquet")

@app.get("/")
def root():
    return {"message": "NFL Awards API is running"}

@app.get("/awards")
def get_awards():
    return df.to_dict(orient="records")
