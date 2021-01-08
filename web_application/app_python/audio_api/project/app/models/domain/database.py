from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://app_user:password@postgres:5432/app_db"

# データベース接続用のインスタンスを作成
# 内部でConnectionというクラスを呼び出してDBとのコネクションを張っている
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 上記のインスタンスを使ってセッションを張る
# SQLAlchemyでORMを実行するにはセッションを作成する必要がある
# セッションは一つのコネクションを使いまわして、ORMを通して色々なSQLクエリを実行する
# ORMを使用しないならいらない
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# ベースモデルというものを作成。これがテーブルの元になる
# ORMを使用するときに使う。ORMを使用しないならいらない(多分)
Base = declarative_base()
Base.query = SessionLocal.query_property()  # ORMを使った検索クエリ(select)をより直感的に使いやすくするもの


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
