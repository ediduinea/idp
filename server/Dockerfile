FROM python:3
EXPOSE 5000
COPY requirements.txt /opt
COPY go.py /opt
COPY templates /opt/templates
COPY static /opt/static
RUN pip install -r /opt/requirements.txt
CMD [ "python3", "/opt/go.py" ]
