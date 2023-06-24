from fastapi import FastAPI
from .services.tasks.controller import router as task_router

app = FastAPI()
app.include_router(task_router)


@app.get("/")
async def health_check():
    return {"status": 200, "message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8020, reload=True)
