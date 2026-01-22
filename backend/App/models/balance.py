from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .user import User  # ← Explicit import here

class Balance(Base):
    __tablename__ = "balances"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False, index=True)  # ← Use User.id (class ref)
    coin = Column(String(10), nullable=False, index=True)
    amount = Column(Numeric(precision=36, scale=18), default=0.0, nullable=False)

    user = relationship("User", back_populates="balances")