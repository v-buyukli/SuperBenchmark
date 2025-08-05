import uvicorn
from fastapi import FastAPI

from src.app.api.routes import router
from src.app.config import settings


app = FastAPI(title='SuperBenchmark')

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('src.app.main:app', host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
