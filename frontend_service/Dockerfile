FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar arquivos proto compilados do backend
COPY --from=backend_service /app/protos/*.py ./protos/ 2>/dev/null || true

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
