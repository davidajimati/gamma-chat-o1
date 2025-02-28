from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

# User
class UserSchema(BaseModel):
    # id: str | None = None  # MongoDB _id (string)
    username: constr(strip_whitespace=True, min_length=1)
    # email: EmailStr
    created_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True


class UserDB(UserSchema):
    id: str         # Database-generated unique identifier

# Message
class MessageSchema(BaseModel):
    user_id: str  # References User _id
    message: str
    response: str
    session_id: str
    timestamp: datetime = datetime.utcnow()

    class Config:
        from_attributes = True


class MessageDB(MessageSchema):
    id: str 


# Summary
class TitleSchema(BaseModel):
    user_id: str  # References User _id
    session_id: str
    title: str
    timestamp: datetime = datetime.utcnow()

    class Config:
        from_attributes = True

class TitleDB(TitleSchema):
    id: str 