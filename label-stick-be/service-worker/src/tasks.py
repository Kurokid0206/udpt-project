from utils.common import check_connection
from celery import Celery
from configs import celery as celery_config
from celery.utils.log import get_task_logger
from kombu import Queue
import json

from celery.utils.log import get_task_logger
from .utils.mail import send_mail

if not check_connection():
    exit()

app = Celery(
    "tasks", broker=celery_config.BROKER_URL, backend=celery_config.BACKEND_URL
)
logger = get_task_logger(__name__)


@app.task(name="send", bind=True)
def send(self, msg):
    data = json.loads(msg)
    send_mail(data)

    return -1
