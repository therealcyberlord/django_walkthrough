FROM python:3.8.13-bullseye

ARG secret_key
ARG api_key
ARG PORT
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

# Run migrations
CMD ["python" "manage.py" "makemigrations"]
CMD ["python" "manage.py" "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]