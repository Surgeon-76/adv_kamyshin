FROM python:3.12

# RUN apt install -y curl
# # RUN curl -sSL https://install.python-poetry.org | python
# RUN curl -sSL https://install.python-poetry.org | python3 -
# # ENV PATH="${PATH}:~/local/bin"
# RUN ls -a


WORKDIR /api

COPY . .
RUN pip --proxy="http://172.21.163.9:3129" install --upgrade pip setuptools wheel
RUN pip --proxy="http://172.21.163.9:3129" install poetry
RUN poetry config virtualenvs.in-project true

WORKDIR ../
RUN poetry install








#####################################
# RUN pip cache purge
# RUN pip install --upgrade pip setuptools wheel
# RUN pip install -r requirements.txt
# RUN pip --proxy="http://172.21.163.9:3129" install --upgrade pip setuptools wheel
# RUN pip --proxy="http://172.21.163.9:3129" install -r requirements.txt
