from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Obligation(Base):
    __tablename__ = "obligations"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    title = Column(String(255))
    description = Column(String(500))
    due_date = Column(Date)
    priority = Column(String(20))
    status = Column(String(50))
    assigned_to = Column(Integer, ForeignKey("users.id"))

    contract = relationship("Contract", back_populates="obligations")   