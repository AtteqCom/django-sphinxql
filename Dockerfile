FROM ubuntu:20.04

RUN apt update && apt install -y build-essential libmysqlclient-dev mysql-server python3-dev python3-venv sphinxsearch sudo

RUN useradd --shell /bin/bash -u 1000 user && \
    mkdir -p /home/user/.ssh && \
    chown user -R /home/user && \
    apt-get install -y sudo && \
    adduser user sudo && \
    echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN mkdir /opt/sphinx && \
    chown user:user /opt/sphinx && \
    mkdir /django-sphinxql

CMD sleep infinity
