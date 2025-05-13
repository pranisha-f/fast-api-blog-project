from sqlalchemy.orm import Session
from db.models.user import User
from schemas.user import UserCreate
from core.hashing import Hasher


def create_user_in_db(db: Session, user: UserCreate) :
    db_user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user