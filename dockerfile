FROM python:3.9-slim

WORKDIR /app

# system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# ✅ STEP 1: requirements file copy karo
COPY requirements.txt .

# ✅ STEP 2: dependencies install karo
RUN pip install --upgrade pip \
    && pip install "setuptools<60" "wheel<0.38" \
    && pip install -r requirements.txt

# ✅ STEP 3: baqi project copy karo
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]