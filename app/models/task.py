from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class Task(Base):  # модель Task, наследованную от ранее написанного Base
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)  # внешний ключ на id из таблицы 'users'

    user = relationship('User', back_populates='tasks')  # объект связи с таблицей User


print(CreateTable(Task.__table__))
