from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./my.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# check_same_threadはSQLITEのみ必要
# デフォルトでは、各スレッドが独立したリクエストを処理することを前提として、SQLiteは1つのスレッドのみがSQLiteと通信できるようにします。

