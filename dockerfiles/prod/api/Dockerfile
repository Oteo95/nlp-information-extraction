FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./src/ /app/src
COPY ./dockerfiles/ /app/dockerfiles
COPY ./data/ /app/data
COPY dockerfiles/prod/api/docker-entrypoint.sh /app/bin/docker-entrypoint.sh

ENV APP_HOME=/app
WORKDIR $APP_HOME
ENV PYTHONPATH=/app/src:/app

RUN set -ex; \
    pip3 --no-cache-dir install --requirement /app/dockerfiles/prod/api/requirements.txt
RUN python -m spacy download en_core_web_sm

ENTRYPOINT ["/app/bin/docker-entrypoint.sh"]
