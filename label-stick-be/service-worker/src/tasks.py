from utils.common import check_connection
from celery import Celery
from configs import celery as celery_config
from celery.utils.log import get_task_logger
from kombu import Queue
import json

from celery.utils.log import get_task_logger
from utils.mail import send_mail
from utils.common import save_to_redis

logger = get_task_logger(__name__)

if not check_connection():
    exit()

app = Celery(
    "tasks",
    broker=celery_config.BROKER_URL,
    backend=celery_config.BACKEND_URL,
)

app.conf.task_queues = [Queue(name="tasks", routing_key="task.#")]


@app.task(name="tasks.send_mail", bind=True)
def send(self, task_id: str, data: dict):
    logger.info(f"== API_TASK: {task_id} RUNNING...")
    data = json.loads(data)
    print(data)
    logger.info(data)
    send_mail(data)

    return 1


@app.task(name="tasks.health_check", bind=True)
def health_check(self, task_id: str):
    logger.info(f"== API_TASK: {task_id} RUNNING...")
    data = json.dumps({"status": 200, "message": "OK"})
    save_to_redis(task_id, data)
    return {"status": 200, "message": "OK"}
