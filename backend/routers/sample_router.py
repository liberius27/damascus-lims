from fastapi import APIRouter

router = APIRouter(
    prefix="/samples",
    tags=["Samples"]
)

@router.get("/")
def get_samples():
    return {"message": "List of samples"}

@router.post("/")
def create_sample():
    return {"message": "Sample created"}