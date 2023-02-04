FROM tiangolo/uvicorn-gunicorn:python3.9-2021-10-02

COPY requirements.txt /requirements/requirements.txt
RUN apt update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements/requirements.txt \
    && rm -rf /requirements

COPY ./ /app
