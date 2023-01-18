import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from lib.hello import hello

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],      
    allow_headers=["*"]       
)
@app.get("/")
async def hello_api():
    return {"message":hello()}


if __name__ == "__main__":
    uvicorn.run(app)