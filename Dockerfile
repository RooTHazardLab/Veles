FROM python:3.10-slim-bookworm

WORKDIR /veles_bot

COPY requirements/prod.txt requirements/prod.txt 

RUN pip install -r requirements/prod.txt 

COPY veles veles

CMD ["python3", "veles/main.py"]
