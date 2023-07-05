from fastapi import UploadFile
from minio import Minio
from datetime import datetime
import os

STORAGE_HOST = os.environ.get("STORAGE_HOST", "103.176.179.83")
STORAGE_PORT = os.environ.get("STORAGE_PORT", "8333")
HOST_PORT = os.environ.get("HOST_PORT", "8888")

client = Minio(
    endpoint=f"{STORAGE_HOST}:{STORAGE_PORT}",
    secure=False,
)


def health_check_minio():
    found = client.bucket_exists("udpt")

    if not found:
        client.make_bucket("udpt")
    else:
        print("Bucket 'udpt' already exists")
    return


def put_object(key: str, file: UploadFile):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    file_extension = file.filename.split(".")[1]

    object_path = f"{key}/{str(ts).split('.')[0]}.{file_extension}"

    client.put_object(
        "udpt", object_path, data=file.file, length=-1, part_size=5 * 1024 * 1024
    )

    return f"/buckets/udpt/{object_path}"
