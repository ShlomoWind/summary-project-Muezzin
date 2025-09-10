FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY ./src app/metadata_handling/src
COPY ../utils app/utils

EXPOSE 8000

CMD ["python", "metadata_handling/src/main.py"]