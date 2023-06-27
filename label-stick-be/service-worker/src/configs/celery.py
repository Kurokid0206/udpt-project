import os

BROKER_URL = os.environ.get('BROKER_URL', 'redis://:redis@localhost:6379/0')

BACKEND_URL = os.environ.get('BACKEND_URL', 'redis://:redis@localhost:6379/1')

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Saigon'
enable_utc = True
