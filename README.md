# RESTful API Hands-On Exercise

This hands-on practice will guide you through building a RESTful API using Python. You will:

✅ Set up a Python REST API (FastAPI or Flask)  
✅ Create CRUD endpoints (GET, POST, PUT, DELETE)  
✅ Connect to a database (SQLite/PostgreSQL)  
✅ Add authentication (JWT tokens)  
✅ Test the API (Postman, PyTest, Unittest)  
✅ Document the API (Swagger UI & OpenAPI)  

## Prerequisites

- Python 3.8+
- Git & GitHub account
- Virtual environment (venv or conda)
- Postman or Curl

## Project Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/restful-api-exercise.git
   cd restful-api-exercise
   ```

2. **Create a virtual environment and activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   Choose your framework: **FastAPI** or **Flask**
   
   - **FastAPI**
     ```sh
     pip install fastapi uvicorn sqlalchemy alembic pydantic passlib python-jose
     ```
   - **Flask**
     ```sh
     pip install flask flask_sqlalchemy flask_jwt_extended flask_swagger_ui
     ```

## Project Structure

```
/restful-api-exercise
├── src/
│   ├── __init__.py  # Marks `src` as a package
│   ├── main.py  # FastAPI entry point
│   ├── routes/
│   │   ├── __init__.py  # Makes `routes` a package
│   │   ├── book_routes.py  # Routes for books API
│   │   ├── user_routes.py  # Routes for user management
│   ├── models/
│   │   ├── __init__.py  # Makes `models` a package
│   │   ├── book_models.py  # Database models for books
│   │   ├── user_models.py  # Database models for users
│   ├── auth/
│   │   ├── __init__.py  # Makes `auth` a package
│   │   ├── jwt_handler.py  # JWT authentication functions
│   ├── database.py  # Database connection
├── tests/
│   ├── test_main.py  # API tests
│   ├── test_auth.py  # Authentication tests
├── requirements.txt  # Dependencies
├── .env  # Environment variables (e.g., database URL, secret keys)
├── README.md  # Project documentation
├── .gitignore  # Ignore unnecessary files
└── Dockerfile  # Docker configuration

## Running the API

### FastAPI
```sh
uvicorn src.main:app --reload
```
API docs available at: `http://127.0.0.1:8000/docs`

### Flask
```sh
python src/main.py
```
API docs available at: `http://127.0.0.1:5000/swagger`

## CRUD Endpoints

| Method | Endpoint        | Description |
|--------|----------------|-------------|
| GET    | `/users`        | Get all users |
| POST   | `/users`       | Create a user |
| GET    | `/users/{id}`  | Get user by ID |
| PUT    | `/users/{id}`  | Update user |
| DELETE | `/users/{id}`  | Delete user |

## Database Configuration

- SQLite (default) or PostgreSQL
- Set up connection in `database.py`

## Authentication

- Uses JWT tokens for secure API access
- Obtain token by logging in via `/auth/login`
- Send token in `Authorization: Bearer <token>` header

## Testing the API

- **Postman**: Import API collection and test endpoints manually
- **PyTest**: Run automated tests
  ```sh
  pytest tests/
  ```

## Deployment

- **Docker**: Build and run containerized API
  ```sh
  docker build -t restful-api .
  docker run -p 8000:8000 restful-api
  ```
- **Cloud Platforms**: Deploy on AWS, Heroku, or DigitalOcean

## Contributing

1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

