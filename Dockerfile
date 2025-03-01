FROM python:3.9-slim

# Install poppler-utils
RUN apt-get update && apt-get install -y poppler-utils

# Install your Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD [\"streamlit\", \"run\", \"app.py\", \"--server.port=8080\", \"--server.address=0.0.0.0\"]
