from sqlalchemy.orm import Mapped,mapped_column
from app.db.database import Base

class Users(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username:Mapped[str] = mapped_column(unique=True,nullable = False)
    name:Mapped[str] = mapped_column(nullable = False)
    gender:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(unique=True,nullable = False)
    hashed_password:Mapped[str] = mapped_column(nullable=False)
    phone:Mapped[str] = mapped_column(unique=True,nullable = False)
