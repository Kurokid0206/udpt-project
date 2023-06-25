import logging
import os
from json import JSONDecodeError
import json
import requests
from enum import Enum
from typing import Optional, Union

from .validation import (
    ValidationError,
    ValidationCodeEnum,
)


class HttpMethod(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"


async def call_api(
    url: str,
    method: HttpMethod = HttpMethod.GET,
    headers: dict = None,
    data: Optional[Union[dict, str]] = None,
    files: dict = None,
    params: dict = None,
    json: dict = None,
) -> dict:
    headers = headers or {"Content-Type": "application/json"}

    response = requests.request(
        method,
        url,
        data=data,
        files=files,
        headers=headers,
        params=params,
        json=json,
    )

    try:
        if not response.ok:
            raise ValidationError(
                ValidationCodeEnum.ERR_COM_000,
                error_fields=[response.json()],
            )

        return response.json()
        return {
            "status_code": 200,
            "message": "success",
            "data": response.json(),
        }

    except JSONDecodeError as e:
        print(e)

    return None
