from sqlalchemy.orm.session import Session
from .schemas import UserBase, PostBase
from .models import User, Post

def create_article(db: Session, request: ArticleBase):
    new_article = Article(
        title = request.title,
        content = request.content,
        is_display = request.is_display
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
