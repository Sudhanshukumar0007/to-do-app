from fastapi import APIRouter,Depends
from app.models.user import UserCreate,UserLogin
from app.services.user_service import register_user,user_login
from sqlalchemy.orm import Session
from app.db.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/auth",tags=["Auth"])
@router.post("/register")
async def register(user:UserCreate,db:Session = Depends(get_db)):
    return register_user(user,db)

@router.post("/login")
async def login(form_data:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    return user_login(form_data.username,form_data.password, db)
