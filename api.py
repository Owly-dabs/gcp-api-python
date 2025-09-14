from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class Response(BaseModel):
    message: str

class NameRequest(BaseModel):
    name: str

@app.get("/")
def hello(name: str = "World"):
   """Return a friendly HTTP greeting."""
   return Response(message=f"Hello, {name}!")

@app.post("/message")
def create_message(request: NameRequest):
    """Create a personalized message."""
    return Response(message=f"Hello, {request.name}!")
    
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))