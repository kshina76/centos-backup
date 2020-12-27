from fastapi import APIRouter, Response, Cookie, Depends, Request
from sqlalchemy.orm import Session
from typing import Optional


from api.dependencies.users import check_session_key
from models.domain.database import get_db

router = APIRouter()


@router.post("")
async def create_post(
    response: Response,
    request: Request,
    db: Session = Depends(get_db),
):
    check_session = check_session_key(db, request.headers["Cookie"])  # セッションチェック
    return check_session
