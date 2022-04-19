from fastapi import APIRouter

router = APIRouter()


@router.get("/items")
async def items():
    return {
        "eggs": 12,
        "spam": 10,
    }
