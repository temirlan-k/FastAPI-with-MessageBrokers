import uvicorn
from fastapi import FastAPI
from app.config.celery_conf.create_celery import create_celery
from app.routers.router import router

def create_app()->FastAPI:
    backend_app = FastAPI(title='Async tasks processing with Celery and RabbitMQ',
                          version="1.0.0",)
    
    backend_app.celery_app = create_celery()
    backend_app.include_router(router=router)
    return backend_app

app = create_app()
celery = app.celery_app

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
