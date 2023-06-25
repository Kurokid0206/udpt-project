import logging
from enum import Enum
import json

log = logging.getLogger(__name__)


class ValidationStatusEnum(Enum):
    OK = "OK"
    ERROR = "ERROR"
    WARNING = "WARNING"


class ValidationCodeEnum(Enum):
    ERR_COM_000 = "Internal error: {}"


class ValidationError(Exception):
    def __init__(
        self,
        validation_code: ValidationCodeEnum,
        error_fields: list[str] = [],
    ):
        self.code = validation_code.name
        self.message = validation_code.value.format(error_fields)
