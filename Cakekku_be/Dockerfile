FROM python:3.10.10

WORKDIR /summerthon_cakekku_be/Cakekku_be

COPY requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Cakekku_be.wsgi:application"]

EXPOSE 8000
