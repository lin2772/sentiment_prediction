from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is IDS721 22Spring Group Project. Weilie Lin, Bohan Li, Yubo Ding"}
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0') 