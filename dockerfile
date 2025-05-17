FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .

CMD echo "Servidor python iniciado correctamente" && python server.py