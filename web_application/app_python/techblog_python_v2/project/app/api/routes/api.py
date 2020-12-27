from fastapi import APIRouter

from api.routes import authentication, posts


router = APIRouter()


# ここにルーティングを追加していく
router.include_router(authentication.router, prefix="")  # 認証
router.include_router(posts.router, prefix="/posts")  # 記事のCRUD
