FROM python:3.8.6-buster
WORKDIR /ingest_service
ADD . /ingest_service
RUN pip install -r requirements.txt
CMD [ "python", "broker_ingest.py" ]