from pydantic import BaseModel, EmailStr
from datetime import datetime
# from bson import ObjectId

class UserSchema(BaseModel):
    # id: str | None = None  # MongoDB _id (string)
    username: str
    email: EmailStr
    created_at: datetime = datetime.utcnow()

    class Config:
        orm_mode = True


class UserDB(UserSchema):
    id: str                                                     # Database-generated unique identifier

class MessageSchema(BaseModel):
    # id: str | None = None
    user_id: str  # References User _id
    message: str
    response: str
    session_id: str
    timestamp: datetime = datetime.utcnow()

    class Config:
        orm_mode = True


class MessageDB(MessageSchema):
    id: str  