from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    contract_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    category = Column(String(100), nullable=False)

    description = Column(String(500))

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    status = Column(
        String(50),
        default="Draft",
        nullable=False
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship(
        "User",
        back_populates="contracts",
        passive_deletes=True
    )

    contract_versions = relationship(
        "ContractVersion",
        back_populates="contract"
    )

    obligations = relationship(
        "Obligation",
        back_populates="contract"
    )

    renewal = relationship(
        "Renewal",
        back_populates="contract",
        uselist=False
    )

    notifications = relationship(
        "Notification",
        back_populates="contract"
    )

    activities = relationship(
        "Activity",
        back_populates="contract"
    )