from sqlalchemy.orm import Session
from apps import models, schemas

#Барлық кітаптарды алу
def get_books(db: Session):
    return db.query(models.Book).all()

#Айди арқылы кітап табу
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

#Жаңа кітап қосу
def create_book(db: Session, book: schemas.BookCreate):
    new_book = models.Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

#Кітапты жаңарту
def update_book(db: Session, book_id: int, updated: schemas.BookCreate):
    db_book = get_book(db, book_id)
    if db_book:
        db_book.title = updated.title
        db_book.author = updated.author
        db_book.year = updated.year
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

#Кітапты жою
def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False

    