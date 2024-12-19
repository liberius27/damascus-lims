from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sample_data = [
    {"id": 1, "name": "Sample A", "status": "Completed"},
    {"id": 2, "name": "Sample B", "status": "Pending"},
    {"id": 3, "name": "Sample C", "status": "In Progress"}
]

@app.get("/samples")
def get_samples():
    return sample_data