FROM python:3.10-slim AS base
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip

FROM base AS base-venv
COPY requirements.txt /requirements.txt
RUN  /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM base-venv AS build-venv
ENV PATH="/venv/bin:$PATH"
COPY pyproject.toml /pyproject.toml
COPY poetry.lock /poetry.lock
RUN  poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


FROM python:3.10-slim
COPY --from=build-venv /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY . /app/service-gateway
WORKDIR /app/service-gateway
ENTRYPOINT ["uvicorn", "src.main", "--host", "0.0.0.0", "--port", "8010", "--reload"]
