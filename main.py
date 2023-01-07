import uvicorn
from typing import Union
from fastapi import FastAPI
from routers import user as UserRouter
from models import user
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=3)

