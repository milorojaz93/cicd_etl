FROM python:3.10-slim

WORKDIR /app

COPY libs.txt .
RUN pip install --no-cache-dir -r libs.txt
RUN mkdir /logs/
COPY api.py .
EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]