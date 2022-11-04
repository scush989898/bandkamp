FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

# remover quando colocar docker compose
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]