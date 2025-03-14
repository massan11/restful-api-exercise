from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.book_models import Book

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/")
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
