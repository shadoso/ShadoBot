FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3-pip \
    build-essential \
    libpq-dev \
    && apt-get clean

WORKDIR /main

ENV PYTHONPATH="${PYTHONPATH}:/main"

COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.12", "main/shadobot.py"]
