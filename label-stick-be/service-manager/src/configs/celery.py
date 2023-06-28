import os

BROKER_URL = os.environ.get("BROKER_URL", "redis://@localhost:6379/0")

BACKEND_URL = os.environ.get("BACKEND_URL", "redis://@localhost:6379/1")

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Asia/Saigon"
enable_utc = True


class RedisBase:
    host: str = os.environ.get("REDIS_HOST", "localhost")
    port: int = os.environ.get("REDIS_PORT", 6379)
    backend_db_name: int = os.environ.get("BACKEND_DB_NAME", 0)
    broker_name: int = os.environ.get("BROKER_NAME", 1)

    def get_redis_queue(self):
        return "redis://{self.hostname}:{self.port}/{self.broker_name}"

    def get_redis_backend(self):
        return "redis://{self.hostname}:{self.port}/{self.broker_name}"
