FROM python:3.5
MAINTAINER Forest Dussault, forest.dussault@inspection.gc.ca

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

COPY ./compose/local/django/celery/worker/start.sh /start-celeryworker.sh
RUN sed -i 's/\r//' /start-celeryworker.sh
RUN chmod +x /start-celeryworker.sh

COPY ./compose/local/django/celery/beat/start.sh /start-celerybeat.sh
RUN sed -i 's/\r//' /start-celerybeat.sh
RUN chmod +x /start-celerybeat.sh

# Genesippr setup
COPY ./compose/local/django/genesipprv2/start.sh /start-genesipprv2.sh
RUN sed -i 's/\r//' /start-genesipprv2.sh
RUN chmod +x /start-genesipprv2.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
