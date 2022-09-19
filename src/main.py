from fastapi import FastAPI

from utils import get_data

app = FastAPI()


@app.get("/news/all")
async def get_news():
    data = get_data()
    return data
