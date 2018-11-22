FROM python:2

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip

WORKDIR /usr/src/app
RUN mkdir output cache
VOLUME ["/usr/src/app/output", "/usr/src/app/cache"]

COPY ./config/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY ./src/* ./

RUN flake8 ./*

COPY ./config/key.json ./

CMD ["./run"]
