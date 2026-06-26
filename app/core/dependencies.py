from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from fastapi.security import OAuth2PasswordBearer
from app.services.auth_service import decode_access_token
from app.services.user_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    email = decode_access_token(token)
    if not email:
        raise HTTPException(status_code=401,detail="Invalid token")
    user = get_user_by_email(email,db)
    return user