from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.renewal import Renewal
from app.schemas.renewal_schema import RenewalCreate, RenewalResponse


router = APIRouter(
    prefix="/renewals",
    tags=["Renewals"]
)


@router.post(
    "",
    response_model=RenewalResponse,
    status_code=status.HTTP_201_CREATED
)
def create_renewal(
    renewal_data: RenewalCreate,
    db: Session = Depends(get_db)
):
    renewal = Renewal(
        contract_id=renewal_data.contract_id,
        renewal_date=renewal_data.renewal_date,
        reminder_days=renewal_data.reminder_days,
        status=renewal_data.status
    )

    db.add(renewal)
    db.commit()
    db.refresh(renewal)

    return renewal


@router.get(
    "/",
    response_model=list[RenewalResponse]
)
def get_renewals(
    db: Session = Depends(get_db)
):
    return db.query(Renewal).all()


@router.get(
    "/{renewal_id}",
    response_model=RenewalResponse
)
def get_renewal(
    renewal_id: int,
    db: Session = Depends(get_db)
):
    renewal = db.query(Renewal).filter(
        Renewal.id == renewal_id
    ).first()

    if not renewal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Renewal not found"
        )

    return renewal