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
    
    Note: This is a demonstration endpoint showing the usage of the requests library.
    In production, implement more comprehensive URL validation and security measures.
    
    Args:
        url: The URL to fetch (without http:// or https://)
    
    Returns:
        Information about the HTTP request
    """
    # SSRF protection: block private IP ranges and localhost
    # This is a basic protection - production systems should use more comprehensive validation
    blocked_patterns = [
        "127.0.0.1", "localhost", "0.0.0.0", 
        "169.254",  # Link-local addresses
        "10.",      # Private network 10.0.0.0/8
        "172.16", "172.17", "172.18", "172.19", "172.20", "172.21", "172.22", 
        "172.23", "172.24", "172.25", "172.26", "172.27", "172.28", "172.29",
        "172.30", "172.31",  # Private network 172.16.0.0/12
        "192.168"   # Private network 192.168.0.0/16
    ]
    
    url_lower = url.lower()
    for pattern in blocked_patterns:
        if pattern in url_lower:
            return {
                "error": "Access to private or local addresses is not allowed",
                "reason": "SSRF protection"
            }
    
    # Additional check for common localhost representations
    if url_lower.startswith("0") or "[::]" in url_lower:
        return {
            "error": "Access to private or local addresses is not allowed",
            "reason": "SSRF protection"
        }
    
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
