from fastapi import FastAPI
import requests

app = FastAPI(
    title="FastAPI Quick Starter",
    description="A simple FastAPI application quickstart",
    version="1.0.0"
)


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {
        "message": "Welcome to FastAPI Quick Starter!",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}


@app.get("/fetch/{url:path}")
async def fetch_url(url: str):
    """
    Example endpoint that uses the requests library to fetch data from an external URL.
    
    Args:
        url: The URL to fetch (without http:// or https://)
    
    Returns:
        Information about the HTTP request
    """
    try:
        full_url = f"https://{url}"
        response = requests.get(full_url, timeout=5)
        return {
            "url": full_url,
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content_length": len(response.content)
        }
    except Exception as e:
        return {
            "error": str(e),
            "url": url
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
