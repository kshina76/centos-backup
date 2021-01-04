from fastapi import APIRouter, Response, Depends, HTTPException
from sqlalchemy.orm import Session

from models.schemas import users as user_schemas
from models.domain import users as user_domains
from api.dependencies.users import get_user
from api.dependencies.session import create_session
from models.domain.database import get_db
from resources import strings


router = APIRouter()


@router.post("/register")
async def register():
    return {"test": "test"}


# データベースに存在するユーザかを問い合わせて、存在したらクッキーにセッションIDを入れる
@router.post("/login")
async def login(
    user: user_schemas.AuthUser, response: Response, db: Session = Depends(get_db)
):
    try:
        db_user = get_user(db, user.email, user.hashed_password)
    except Exception:
        raise HTTPException(status_code=404, detail=strings.USER_DOES_NOT_EXIST_ERROR)

    response.set_cookie(key="session-key", value="fake-session-key", httponly=True)
    create_session(db, "session-key=fake-session-key", user.email, user.user_name)
    return db_user
