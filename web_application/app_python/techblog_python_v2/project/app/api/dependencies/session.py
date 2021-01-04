from fastapi import Response
from sqlalchemy.orm import Session

from models.domain import users as user_domains
from models.domain import session as user_session


def create_session(db: Session, session_id: str, user_email: str, user_name: str):
    db_session = user_session.UserSession(
        sess_id=session_id, email=user_email, user_name=user_name
    )
    db.add(db_session)
    db.commit()
