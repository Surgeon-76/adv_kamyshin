FROM python:3.11

WORKDIR /api

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip --proxy="http://172.21.163.9:3129" install --upgrade pip 
# RUN pip --proxy="http://172.21.163.9:3129" install -r requirements.txt 
