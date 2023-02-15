FROM python:3.10-slim

WORKDIR . /nyria

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "./nyria.py"]
