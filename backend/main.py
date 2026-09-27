from fastapi import FastAPI

from schemas.response import APIResponse


app = FastAPI()


@app.get("/", response_model=APIResponse[dict])
async def root():
    return APIResponse(
        success=True,
        data={"message": "Backend is alive 🔥"},
    )