import os


class RedisBase():
    host: str = os.environ.get('REDIS_HOST', 'localhost')
    port: int = os.environ.get('REDIS_PORT', 6379)
    password: str = os.environ.get('REDIS_PASSWORD', 'redis')
    backend_db_name: int = os.environ.get('BACKEND_DB_NAME', 0)
    broker_name: int = os.environ.get('BROKER_NAME', 1)

    def get_redis_queue(self):
        return "redis://:{self.password}@{self.hostname}:{self.port}/{self.broker_name}"

    def get_redis_backend(self):
        return "redis://:{self.password}@{self.hostname}:{self.port}/{self.broker_name}"
