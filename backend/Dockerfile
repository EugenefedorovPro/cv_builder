FROM python:3.12.1-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY ../requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint*.sh

