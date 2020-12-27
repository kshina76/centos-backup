from fastapi import Response
from sqlalchemy.orm import Session

from models.domain import users as user_domains
from models.domain import session as user_session


# emailとhashed_passwordで問い合わせて、ユーザを取得する
def get_user(db: Session, email: str, hashed_password: str):
    return (
        db.query(user_domains.User)
        .filter(
            user_domains.User.email == email,
            user_domains.User.hashed_password == hashed_password,
        )
        .one()
    )


def check_session_key(db: Session, sess_id: str):
    db_session = (
        db.query(user_session.UserSession)
        .filter(user_session.UserSession.sess_id == sess_id)
        .one()
    )
    return db_session
