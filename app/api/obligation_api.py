from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.obligation import Obligation
from app.schemas.obligation_schema import (
    ObligationCreate,
    ObligationResponse
)


router = APIRouter(
    prefix="/obligations",
    tags=["Obligations"]
)


@router.post(
    "",
    response_model=ObligationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_obligation(
    obligation_data: ObligationCreate,
    db: Session = Depends(get_db)
):
    obligation = Obligation(
        contract_id=obligation_data.contract_id,
        title=obligation_data.title,
        description=obligation_data.description,
        due_date=obligation_data.due_date,
        priority=obligation_data.priority,
        status=obligation_data.status,
        assigned_to=obligation_data.assigned_to
    )

    db.add(obligation)
    db.commit()
    db.refresh(obligation)

    return obligation


@router.get(
    "/",
    response_model=list[ObligationResponse],
    status_code=status.HTTP_200_OK
)
def get_obligations(
    db: Session = Depends(get_db)
):
    return db.query(Obligation).all()


@router.get(
    "/{obligation_id}",
    response_model=ObligationResponse,
    status_code=status.HTTP_200_OK
)
def get_obligation(
    obligation_id: int,
    db: Session = Depends(get_db)
):
    obligation = db.query(Obligation).filter(
        Obligation.id == obligation_id
    ).first()

    if not obligation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Obligation not found"
        )

    return obligation