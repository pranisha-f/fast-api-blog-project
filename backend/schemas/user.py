from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr 
    password: str = Field(..., min_length=8, max_length=128)

class UserResponse(BaseModel):
    id: int
    email: EmailStr 
    is_active: bool = True

    class Config:
      
        orm_mode = True