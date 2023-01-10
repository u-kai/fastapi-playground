import uvicorn
from fastapi import FastAPI

from lib.hello import hello

app = FastAPI()

@app.get("/")
async def hello_api():
    return {"message":hello()}


if __name__ == "__main__":
    uvicorn.run(app)