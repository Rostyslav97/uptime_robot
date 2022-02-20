FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY . .

# Install deps requirements
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install poetry \
    && poetry config virtualenvs.create false

RUN poetry install

CMD python manage.py migrate --noinput \
    && python manage.py runserver 0.0.0.0:8000