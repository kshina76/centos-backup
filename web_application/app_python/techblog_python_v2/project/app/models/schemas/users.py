from pydantic import BaseModel


class User(BaseModel):
    email: str
    hashed_password: str
    user_name: str

    class Config:
        orm_mode = True


class AuthUser(User):
    pass


class LoginUser(User):
    pass
