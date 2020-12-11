FROM python:3.8.6-buster
WORKDIR /data_ingest_service
ADD . /data_ingest_service
RUN pip install -r requirements.txt
CMD [ "python", "ingest.py" ]

