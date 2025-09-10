FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY metadata_handling/src app/metadata_handling/src

CMD ["python", "main.py"]