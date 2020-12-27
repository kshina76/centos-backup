from fastapi import APIRouter, Response, Depends
from sqlalchemy.orm import Session

from models.schemas import users as user_schemas
from models.domain import users as user_domains
from api.dependencies.users import get_user
from api.dependencies.session import create_session
from models.domain.database import get_db


router = APIRouter()


@router.post("/register")
async def register():
    return {"test": "test"}


# データベースに存在するユーザかを問い合わせて、存在したらクッキーにセッションIDを入れる
@router.post("/login", response_model=user_schemas.LoginUser)
async def login(
    user: user_schemas.AuthUser, response: Response, db: Session = Depends(get_db)
):
    db_user = get_user(db, user.email, user.hashed_password)
    if db_user:
        response.set_cookie(key="session-key", value="fake-session-key", httponly=True)
        create_session(db, "session-key=fake-session-key", user.email)
        return db_user
    return db_user
