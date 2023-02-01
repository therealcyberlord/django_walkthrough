FROM python:3.8.13-bullseye

ARG secret_key
ARG api_key
ARG PORT

WORKDIR /my_project/

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]