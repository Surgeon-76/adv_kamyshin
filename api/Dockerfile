FROM python:3.11

WORKDIR /api

COPY . .
RUN pip cache purge
# RUN pip install --upgrade pip setuptools wheel
# RUN pip install -r requirements.txt
RUN pip --proxy="http://172.21.163.9:3129" install --upgrade pip setuptools wheel
RUN pip --proxy="http://172.21.163.9:3129" install -r requirements.txt
