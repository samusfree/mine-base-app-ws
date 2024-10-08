from sqlalchemy import Column, Date, Integer, String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: String = Column(String(50), nullable=False)
    lastname: String = Column(String(50), nullable=False)
    born: Date = Column(Date, nullable=False)
