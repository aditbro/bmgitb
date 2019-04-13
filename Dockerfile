FROM python:3.6
# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    netcat
# Project Files and Settings
WORKDIR /bmgitb
COPY . .
RUN pip install -U pipenv && \
    pipenv install -r requirements.txt && \
    pipenv install --system

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["runserver", "0.0.0.0:8080"]
