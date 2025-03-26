FROM python:3.12.9-bookworm


COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt
COPY . .