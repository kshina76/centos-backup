from sqlalchemy.orm import Session
from models.domain.posts import Post


from datetime import datetime


def create_posts(db: Session, user_name: str, title: str, text: str):
    post = Post(author=user_name, title=title, text=text, created_at=datetime.now())
    db.add(post)
    db.commit()


def get_post(db: Session, author: str):
    if author is not None:
        return db.query(Post).filter(Post.author == author).all()
    return db.query(Post).all()
