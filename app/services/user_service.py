from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import UserCreate,UserResponse
from app.services.auth_service import hash_pwd,verify_pwd,create_access_token
from app.db.models.user import Users

def get_user_by_email(email:str,db:Session) -> Users:
    user = db.query(Users).filter(Users.email==email).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

def register_user(user:UserCreate,db:Session) -> dict:
    existing_email = db.query(Users).filter(Users.email==user.email).first()
    if existing_email:
        raise HTTPException(status_code=400,detail="email already exists")
    existing_username = db.query(Users).filter(Users.username==user.username).first()
    if existing_username:
        raise HTTPException(status_code=400,detail="Username already exists")
    hashed_pwd = hash_pwd(user.password)

    user1 = Users(
        name = user.name,
        username = user.username,
        gender = user.gender,
        email = user.email,
        hashed_password = hashed_pwd,
        phone = user.phone
    )
    db.add(user1)
    db.commit()
    db.refresh(user1)

    response = UserResponse(
        name = user.name,
        username = user.username,
        gender = user.gender,
        email = user.email,
        phone = user.phone
    ) 
    return {
        "message":"User registered successfully",
        "user":response
    }

def user_login(email:str,pwd:str,db:Session) -> dict:
    user = get_user_by_email(email,db)

    if not verify_pwd(pwd,user.hashed_password):
        raise HTTPException(status_code=401,detail="Wrong email or password")
    token = create_access_token({"sub":email})
    return {
        "access_token":token,
        "token_type": "bearer"
    }
