from fastapi import FastAPI
from .services.project.controller import router as project_router
from .services.document.controller import router as document_router
from .utils.storage import health_check_minio
from .utils.celery_worker import celery_worker

app = FastAPI()
app.include_router(project_router)
app.include_router(document_router)


@app.get("/")
async def health_check():
    # health_check_minio()
    celery_worker.send_task(
        name="tasks.health_check",
        kwargs={"task_id": "1"},
        queue="tasks",
    )
    return {"status": 200, "message": "Hello World"}


import json


@app.post("/")
async def send_mail():
    data = json.dumps(
        {
            "from_email": "19120674@student.hcmus.edu.vn",
            "to_email": "kurokid0206@gmail.com",
            "subject": "Test",
            "content": "Test",
        }
    )
    celery_worker.send_task(
        name="tasks.send_mail",
        kwargs={"task_id": "2", "data": data},
        queue="tasks",
    )
    return {"status": 200, "message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8020, reload=True)
