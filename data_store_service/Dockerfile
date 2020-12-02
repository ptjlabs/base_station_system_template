FROM python:3.8.6-buster
WORKDIR /store_service
ADD . /store_service
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]