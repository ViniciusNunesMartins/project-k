FROM python:3.9-slim-bullseye
RUN python -m venv ./venv
RUN . ./venv/bin/activate

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_USER False

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "migrate"]


COPY . .