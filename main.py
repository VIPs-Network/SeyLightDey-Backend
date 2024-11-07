from fastapi import FastAPI

app = FastAPI(title="Shey light Dey", description="This is a simple API created using FastAPI", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello, SLD!"}


if __name__== "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)