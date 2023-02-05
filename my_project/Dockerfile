FROM python:3.9

ARG secret_key
ARG api_key
ARG DATABASE_URL
ARG PGDATABASE
ARG PGHOST
ARG PGPASSWORD
ARG PGPORT
ARG PGUSER

ENV PYTHONBUFFERED=1

WORKDIR /my_project

COPY . .

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]