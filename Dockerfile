FROM python:3.9.6-slim

WORKDIR /opt/app
COPY app.py ./
COPY input.csv ./

COPY entrypoint.sh ./
RUN chmod 777 entrypoint.sh

ENTRYPOINT [ "/opt/app/entrypoint.sh" ]