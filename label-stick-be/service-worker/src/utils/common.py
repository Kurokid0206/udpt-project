from redis import Redis
from configs import base


def check_connection():
    redis_base = base.RedisBase()
    try:
        conn = Redis(
            host=redis_base.host,
            port=redis_base.port,
            db=redis_base.backend_db_name,
            password=redis_base.password,
        )
        conn.client_list()
    except Exception as e:
        print(
            f"Failed to connect to Redis instance at {redis_base.backend_db_name}")
        print(repr(e))
        return False
    finally:
        conn.close()
    return True


def save_to_redis(key, value):
    redis_base = base.RedisBase()
    try:
        conn = Redis(
            host=redis_base.host,
            port=redis_base.port,
            db=redis_base.backend_db_name,
            password=redis_base.password,
        )
        conn.set(key, value)
    except Exception as e:
        print(
            f"Failed to connect to Redis instance at {redis_base.backend_db_name}")
        print(repr(e))
        return False
    finally:
        conn.close()
    return True
