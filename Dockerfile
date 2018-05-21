FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  apt-get clean
RUN pip install uwsgi

ADD . /opt/it_courses
WORKDIR /opt/it_courses

RUN pip install pipenv && pipenv install --system --dev --three

EXPOSE 8000
ENV PORT 8000

CMD python manage.py runserver 0.0.0.0:8000