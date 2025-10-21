FROM python:3.9.23-slim-trixie

WORKDIR /app

COPY ["./RedisTestMain.py", "."]
COPY ["./requirements.txt", "."]

RUN pip install -r requirements.txt

CMD ["python", "RedisTestMain.py"]