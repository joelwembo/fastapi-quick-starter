# Minimal FastAPI starter — optional CI/CD bundle (adjust CMD if your app path differs)
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/docs || curl -f http://localhost:8000/health || exit 1

# Default: common quick-starter layout (override in docker-compose if needed)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
