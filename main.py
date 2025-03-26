import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

fastApiApp = FastAPI()
origins = ["*"]
fastApiApp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictParams(BaseModel):
    a: float
    b: float

@fastApiApp.get("/predict")
async def createMunit(a: float, b: float):
    return a + b


@fastApiApp.post("/predict")
async def createMunit(params: PredictParams):
    a = params.a
    b = params.b

    return a + b

if __name__ == "__main__":
    uvicorn.run(fastApiApp, port=8000)