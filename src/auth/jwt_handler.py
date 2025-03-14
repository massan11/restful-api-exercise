import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")

def create_jwt_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
