from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Renewal(Base):
    __tablename__ = "renewals"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), unique=True)
    renewal_date = Column(Date)
    reminder_days = Column(Integer)
    status = Column(String(50))

    contract = relationship("Contract", back_populates="renewal")