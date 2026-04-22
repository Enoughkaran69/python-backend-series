# pip install fastapi uvicorn ( install these library )

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
  
# py -m uvicorn app:app --reload  (code to run the server)
