from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    contract_number = Column(String(100))
    vendor_name = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    contract_value = Column(Float)
    status = Column(String(50))

    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))

    user = relationship("User", back_populates="contracts", passive_deletes=True)

    contract_versions = relationship("ContractVersion", back_populates="contract")
    obligations = relationship("Obligation", back_populates="contract")
    renewal = relationship("Renewal", back_populates="contract", uselist=False)
    notifications = relationship("Notification", back_populates="contract")
    activities = relationship("Activity", back_populates="contract")