FROM python:3.9-slim-buster

WORKDIR /app

COPY test_app.py .

CMD ["python3", "test_app.py"]
