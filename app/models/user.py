from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Literal

GenderType = Literal["Male", "Female", "Others"]

class UserBase(BaseModel):
    username: Annotated[str, Field(..., description="Username that will be shown", examples=["blackdevil"])]
    name: Annotated[str, Field(..., description="Name of the user", examples=["Sudhanshu Kumar"])]
    gender: Annotated[GenderType, Field(..., description="Gender of User", examples=["Male"])]
    email: Annotated[EmailStr, Field(..., description="Email of User", examples=["blackdevil@gmail.com"])]
    phone: Annotated[str, Field(..., description="Mobile number of the user", examples=["9876543210"])]


class UserCreate(UserBase):
    password: Annotated[str, Field(..., min_length=8, description="User password (min 8 characters)", examples=["supersecret123"])]


class UserResponse(UserBase):
    pass  


class UserUpdate(BaseModel):
    username: str | None = None
    name: str | None = None
    gender: GenderType | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = Field(None, min_length=8, description="New password if updating")
class UserLogin(BaseModel):
    email:str 
    password:str

class TokenData(BaseModel):
    email:str | None = None
class Token(BaseModel):
    access_token:str
    token_type:str = 'bearer'
