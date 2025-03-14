from fastapi import FastAPI
from src.routes import book_routes, user_routes
from src.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="RESTful API Exercise")

# Include API routes
app.include_router(book_routes.router)
app.include_router(user_routes.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the RESTful API!"}