FROM python:latest

RUN mkdir /app
WORKDIR /app
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

# Install project dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5000
EXPOSE 80

WORKDIR /src

CMD gunicorn --bind 0.0.0.0:80 wsgi:app