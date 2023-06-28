from celery import Celery
from configs import celery as celery_config

celery_worker = Celery(backend=celery_config.BACKEND_URL,
                       broker=celery_config.BROKER_URL)
