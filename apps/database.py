# PostgreSQL дерекқорына қосылу параметрлері

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Дерекбазасына сілтеме
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()