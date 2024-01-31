from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Do not go gentle into that good night..."}
