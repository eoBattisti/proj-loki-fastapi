FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir fastapi uvicorn gunicorn python-logging-loki


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
