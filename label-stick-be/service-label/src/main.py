from fastapi import FastAPI
from .services.label.controller import router as label_router
from .services.sentence.controller import router as sentence_router
from .services.label_sentence.controller import router as label_sentence_router

app = FastAPI()
app.include_router(label_router)
app.include_router(sentence_router)
app.include_router(label_sentence_router)


@app.get("/")
async def health_check():
    return {"status": 200, "message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8030, reload=True)
