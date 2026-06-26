from datetime import datetime, timedelta
import bcrypt
from jose import jwt, JWTError
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
def hash_pwd(pwd:str) -> str:
    pwd_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify_pwd(plain_pwd:str,hashed_pwd:str) -> bool:
    try:
        return bcrypt.checkpw(
            plain_pwd.encode('utf-8'),
            hashed_pwd.encode('utf-8')
        )
    except Exception:
        return False

def create_access_token(data:dict) -> str:
    copy_data = data.copy()
    copy_data["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(copy_data,SECRET_KEY,ALGORITHM)
def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
