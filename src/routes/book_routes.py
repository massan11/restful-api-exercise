from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.book_models import Book as BookModel
from src.models.book_schemas import Book, BookCreate

router = APIRouter()

@router.get("/books/", response_model=list[Book])
def read_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books

@router.post("/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book