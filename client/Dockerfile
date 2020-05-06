FROM python:3
COPY requirements.txt /opt
COPY client.py /opt
RUN pip install -r /opt/requirements.txt
CMD [ "python3", "/opt/client.py"]
