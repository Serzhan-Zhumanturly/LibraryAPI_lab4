from fastapi import FastAPI
from apps.routes import books
from apps.database import Base, engine

#Кестеін автоматты түрде құру 
Base.metadata.create_all(bind=engine)

apps = FastAPI(title="Кітапхана API (FastAPI + PostgreSQL)")

# /books маршруттарын қосу
apps.include_router(books.router)

@apps.get("/")
def root():
    return {"message": "Кітапхана APi-ге - қош келдіңіз!"}