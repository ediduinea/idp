FROM python:3.6

EXPOSE 5000

WORKDIR /opt

COPY requirements.txt /opt
RUN pip install -r requirements.txt

COPY admin.py /opt
CMD [ "python3", "/opt/admin.py"]

