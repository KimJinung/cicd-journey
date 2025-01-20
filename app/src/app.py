from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
async def read_greeting():
    return {"message": "Hello, World!"}