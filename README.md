# FastAPI Quick Starter

A simple and clean FastAPI quickstart application with minimal dependencies.

## Features

- Clean FastAPI application structure
- Basic endpoints (root, health check, and example fetch endpoint)
- Only essential dependencies (fastapi and requests)
- Auto-generated interactive API documentation
- Ready to run without Docker

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/joelwembo/fastapi-quick-starter.git
cd fastapi-quick-starter
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Using uvicorn directly
```bash
uvicorn app.app:app --reload
```

### Option 2: Running the Python file directly
```bash
python app/app.py
```

The application will start on `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /fetch/{url}` - Example endpoint that fetches external URLs using the requests library
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## Example Usage

### Using curl
```bash
# Root endpoint
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health

# Fetch example (fetches google.com)
curl http://localhost:8000/fetch/google.com
```

### Using Python requests
```python
import requests

response = requests.get("http://localhost:8000/")
print(response.json())
```

## Project Structure

```
fastapi-quick-starter/
├── app/
│   └── app.py          # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Dependencies

- **fastapi** - Modern, fast web framework for building APIs
- **requests** - HTTP library for making requests
- **uvicorn** - ASGI server for running the application

## Development

To run the application in development mode with auto-reload:
```bash
uvicorn app.app:app --reload --host 0.0.0.0 --port 8000
```

## License

See LICENSE file for details.