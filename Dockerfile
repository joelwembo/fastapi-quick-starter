# Minimal compose for FastAPI quick-starter — optional CI/CD bundle
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "${PORT:-8000}:8000"
    environment:
      - ENVIRONMENT=${ENVIRONMENT:-development}
    restart: unless-stopped
