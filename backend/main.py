from fastapi import FastAPI

app = FastAPI()

# Sample data
sample_data = [
    {"id": 1, "name": "Sample A", "status": "Completed"},
    {"id": 2, "name": "Sample B", "status": "Pending"},
    {"id": 3, "name": "Sample C", "status": "In Progress"}
]

@app.get("/samples")
def get_samples():
    return sample_data