from fastapi import FastAPI, File, Form, UploadFile
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from .utils.storage import put_object

from .GraphQL.schema import schema

graphql_app = GraphQL(schema=schema, graphiql=True)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://udpt.ti-pt.info",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...), project_id: int = Form(...)):
    file_url = put_object(file=file, key=project_id)

    return {"url": file_url}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
