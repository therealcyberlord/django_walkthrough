FROM python:3.8.13-bullseye

ARG secret_key
ARG api_key

WORKDIR /my_project/

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]