from fastapi import APIRouter, Response, Cookie, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from fastapi import Body

from api.dependencies.users import check_session_key
from api.dependencies.posts import create_posts, get_post
from models.domain.database import get_db
from models.domain import posts as PostModel
from models.schemas import posts as PostSchema
from resources import strings

router = APIRouter()


@router.post("")
async def create_post(
    response: Response,
    request: Request,
    post_schema: PostSchema.Post = Body(..., embed=False),
    db: Session = Depends(get_db),
):
    try:
        check_session = check_session_key(db, request.headers["Cookie"])  # セッションチェック
    except Exception:
        raise HTTPException(status_code=404, detail=strings.SESSION_KEY_DOES_NOT_EXIST)

    try:
        post = create_posts(
            db, check_session.user_name, post_schema.title, post_schema.text
        )
    except Exception:
        raise HTTPException(status_code=404, detail=strings.CANNOT_CREATE_POST)

    return post


@router.get("")
async def get_posts(author: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        post = get_post(db, author)
    except Exception:
        raise HTTPException(status_code=404, detail=strings.CANNOT_GET_USER)
    return post
