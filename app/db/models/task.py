from sqlalchemy.orm import Mapped,mapped_column
from app.db.database import Base
from sqlalchemy import ForeignKey
from datetime import date
class Tasks(Base):
    __tablename__ = "tasks"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title:Mapped[str] = mapped_column(nullable=False)
    category:Mapped[str] = mapped_column(nullable=False)
    deadline:Mapped[date] = mapped_column(nullable=False)
    status:Mapped[str] = mapped_column(nullable=False)
    priority:Mapped[str] = mapped_column(nullable=False)