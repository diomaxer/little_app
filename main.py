from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("product/")
async def root():
    return {
        "eggs": 12,
        "spam": 10,
    }
