from fastapi import FastAPI
from src.services.rate_receiver import return_rate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fetch_rate")
async def root():
    rate = return_rate()
    return {"rate": rate}

@app.get("/rate")
async def root():
    return {"message": "Hello World"}