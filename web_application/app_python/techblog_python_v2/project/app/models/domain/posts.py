from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    author = Column(
        String(255),
        ForeignKey(
            "users.name",  # ForeignKeyで<テーブル名>.<参照先のレコード>のように指定する
            ondelete="CASCADE",  # ondeleteは参照先が削除された時に自分自身はどうするかの設定。CASCADEは一緒に削除する設定
        ),
        nullable=False,
    )
    title = Column(String(100), unique=True, nullable=False)
    text = Column(Text, unique=False, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    # tag = Column(String, ForeignKey)
    # category

    relation = relationship("User", back_populates="relation")
