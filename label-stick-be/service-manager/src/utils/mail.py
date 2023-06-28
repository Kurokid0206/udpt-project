from enum import Enum
import json
from typing import List, Union

from pydantic import BaseModel
from .celery_worker import celery_worker


class AssignmentTypeEnum(str, Enum):
    LABEL = "LABEL"
    REVIEW = "REVIEW"
    REVISE = "REVISE"


class SendMailDTO(BaseModel):
    from_email: str = "19120674@student.hcmus.edu.vn"
    to_email: Union[str, List[str]]
    subject: str = "Label Stick - Notification"
    username: str
    project_name: str
    task_type: AssignmentTypeEnum = AssignmentTypeEnum.LABEL
    deadline: str


async def send_mail(data: SendMailDTO):
    tmp = json.dumps(
        {
            "from_email": "19120674@student.hcmus.edu.vn",
            "to_email": "kurokid0206@gmail.com",
            "subject": "Test",
            "username": "Kurokid",
            "project_name": "Test Project",
            "task_type": "labeling",
            "deadline": "2023-05-20 00:00:00",
        }
    )
    celery_worker.send_task(
        name="tasks.send_mail",
        kwargs={"task_id": "2", "data": tmp},
        queue="tasks",
    )
    return {"status": 200, "message": "Mail sent successfully"}
