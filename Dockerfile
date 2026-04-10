# Base image (py) : tell docker to start using this image
FROM python:3.9-alpine3.13
# Tells who created or maintains this image
LABEL maintainer="Joshi Sourabha"

# which make py output shows immediately in logs. Without this o.p might be late
ENV PYTHONBUFFERED=1

#Coping from my s/m to Docker image
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
      --disabled-password \
      --no-create-home \
      djnago-user

ENV PATH="/py/bin:$PATH"

USER django-user