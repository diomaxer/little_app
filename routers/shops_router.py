from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def shops():
    return {
        1: "Product",
        2: "Technic",
        3: "T-shirts"
    }
