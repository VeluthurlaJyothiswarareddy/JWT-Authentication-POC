from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI(
    title="JWT POC",
    description="JWT Authentication POC with FastAPI and MongoDB"
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "JWT POC API"}


# 👇 Add this block at the bottom
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",   # file_name:app_instance
        host="0.0.0.0",
        port=8000,
        reload=True   # auto-reload on code changes (dev only)
    )