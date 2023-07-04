import os

USER_SERVICE_URL = os.environ.get("USER_SERVICE_URL", "http://localhost:8010")
MANAGER_SERVICE_URL = os.environ.get("MANAGER_SERVICE_URL", "http://localhost:8020")
LABEL_SERVICE_URL = os.environ.get("LABEL_SERVICE_URL", "http://localhost:8030")
