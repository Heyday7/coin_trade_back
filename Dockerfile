FROM python:3.8.5

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip3 install pipenv
RUN pipenv install --system

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /

