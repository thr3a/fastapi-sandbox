from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

# models.pyにはSQLAlchemyのクラスを作る
# SQLAlchemyは、「モデル」という用語を使用して、データベースと対話するこれらのクラスおよびインスタンスを指します。
# ただし、Pydanticでは、「モデル」という用語を使用して、データの検証、変換、ドキュメントのクラスとインスタンスなど、別の何かを指します。

# SQLAlchemy は "モデル" という用語を、データベースと相互作用するこれらのクラスやインスタンス を指すのに使っています。
# しかし、Pydantic は "モデル" という用語を、データの検証、変換、文書化のクラスやインスタンスという、別のものを指すのにも使っています。
