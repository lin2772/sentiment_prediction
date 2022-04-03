from fastapi import FastAPI
import uvicorn
import pandas as pd
import mlflow
import json
from pandas.io.json import json_normalize

loaded_model = mlflow.pyfunc.load_model('../model')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is IDS721 22Spring Group Project. Weilie Lin, Bohan Li, Yubo Ding"}

@app.get("/columns/{col}/data/{dat}")
async def callModel(col: str, dat: str):
    dp= pd.DataFrame(eval(dat), columns = [col])
    return {"results": str(loaded_model.predict(dp))}
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0') 