from fastapi import FastAPI
from routers import sample_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sample_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Damascus LIMS Backend"}