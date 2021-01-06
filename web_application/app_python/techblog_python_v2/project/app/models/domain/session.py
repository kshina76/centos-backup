from sqlalchemy import Column, Integer, String

from .database import Base


class UserSession(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    sess_id = Column(String(256), unique=True, nullable=False)
    email = Column(String(128), unique=False, nullable=False)
    user_name = Column(String(255), unique=False, nullable=False)
