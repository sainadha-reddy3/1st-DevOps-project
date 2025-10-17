from fastapi import FastAPI

app = FastAPI()

visits = 0

@app.get("/")
def read_root():
    global visits
    visits += 1
    return {"message":"Hello from Dockerized FastAPI!", "visits": visits}
