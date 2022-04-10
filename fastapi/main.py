from fastapi import FastAPI, Form
import uvicorn
import pandas as pd
import mlflow
import json
from pandas.io.json import json_normalize
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from pathlib import Path
import urllib.parse

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
loaded_model = mlflow.pyfunc.load_model('model')
app = FastAPI(template_folder='template')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('post.html', { 'request': request})

@app.get("/data/{dat}")
async def callModel(dat: str):
    dp= pd.DataFrame(eval(dat), columns = ['tweet'])
    return {"results": str(loaded_model.predict(dp))}

@app.post("/input/")
async def inputForm(request: Request, password: str = Form(...)):
    data = eval(password)
    dp = pd.DataFrame(data, columns = ['tweet'])
    res = str(loaded_model.predict(dp))[1:-1].split(" ")
    resStr = ""
    for i in range(0, len(res)):
        if res[i] == '0':
            resStr += data[i] + ": good speech\n"
            print("here"+ resStr)
        if res[i] == '1':
            resStr += data[i] + ": not good speech\n"
    return templates.TemplateResponse('result.html', { 'request': request, 'username': resStr})
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0') 
    

#message = urllib.parse.quote("['I like it']")
#print(app.url_path_for('callModel', col='tweet', dat=message))
    
    
