import uvicorn
from fastapi import FastAPI
import jwt

from routes import router
from database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router, prefix='/indicator')

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, workers=3)
