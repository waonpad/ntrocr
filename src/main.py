from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


# fastapi dev --host 0.0.0.0 src/main.py
