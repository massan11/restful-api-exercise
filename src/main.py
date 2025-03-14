from fastapi import FastAPI
from src.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my REST API"}

@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/books/")
async def create_book(book: dict):
    return book

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)