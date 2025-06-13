# Dockerfile.web

FROM python:3.11-slim

WORKDIR /app

# Копіюємо код і залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Відкриваємо порт Flask
EXPOSE 5003

# Запускаємо Flask
CMD ["python", "app.py"]
