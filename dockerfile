FROM python:3.9-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --upgrade pip \
    && pip install "setuptools<60" "wheel<0.38" \
    && pip install -r requirements.txt


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]