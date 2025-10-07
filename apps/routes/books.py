# Барлық API маршруты осы файлда
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps import crud, schemas
from apps.database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

#Әр сұраныс сайын дереқордың жаңа сессиясын беру
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Барлық кітаптар
@router.get("/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

#Бір кітап
@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Кітап табылмады")
    return book

#Қосу
@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

#Жаңарту
@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated: schemas.BookCreate, db: Session = Depends (get_db)):
    book = crud.update_book(db, book_id, updated)
    if not book:
        raise HTTPException(status_code=404, detail="Кітап табылмады")
    return book

#Жою 
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Кітап табылмады")
    return {"meassage": "Кітап жойылды"}

