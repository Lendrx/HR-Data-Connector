from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

@app.get("/get_clean_data")
async def get_clean_data():
    try:
        df = pd.read_csv("clean_data.csv")
        data = df.to_dict(orient="records")
        return {"cleaned_data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))