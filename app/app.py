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
def fetch_url(url: str):
    """
    Example endpoint that uses the requests library to fetch data from an external URL.
    
    Note: This is a demonstration endpoint. In production, implement proper URL validation
    and security measures to prevent SSRF attacks.
    
    Args:
        url: The URL to fetch (without http:// or https://)
    
    Returns:
        Information about the HTTP request
    """
    # Basic SSRF protection: block private IP ranges and localhost
    blocked_patterns = ["127.0.0.1", "localhost", "0.0.0.0", "169.254", "10.", "172.16", "192.168"]
    if any(pattern in url.lower() for pattern in blocked_patterns):
        return {"error": "Access to this URL is not allowed"}
    
    try:
        full_url = f"https://{url}"
        response = requests.get(full_url, timeout=5)
        return {
            "url": full_url,
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content_length": len(response.content)
        }
    except Exception:
        return {"error": "Failed to fetch the requested URL"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
