from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    status = Column(String, default="Pending")

    assigned_to = Column(Integer, ForeignKey("users.id"))