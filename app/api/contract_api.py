from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract
from app.schemas.contract_schema import (
    ContractCreate,
    ContractResponse
)
from app.core.auth import get_current_user

router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)


@router.post(
    "",
    response_model=ContractResponse,
    status_code=status.HTTP_201_CREATED
)
def create_contract(
    contract_data: ContractCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check duplicate contract number
    existing = db.query(Contract).filter(
        Contract.contract_number == contract_data.contract_number
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Contract number already exists"
        )

    contract = Contract(
        title=contract_data.title,
        contract_number=contract_data.contract_number,
        category=contract_data.category,
        description=contract_data.description,
        start_date=contract_data.start_date,
        end_date=contract_data.end_date,
        status="Draft",
        created_by=current_user.id
    )

    db.add(contract)
    db.commit()
    db.refresh(contract)

    return contract


@router.get(
    "/",
    response_model=list[ContractResponse],
    status_code=status.HTTP_200_OK
)
def get_contracts(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contracts = db.query(Contract).all()
    return contracts


@router.get(
    "/{contract_id}",
    response_model=ContractResponse,
    status_code=status.HTTP_200_OK
)
def get_contract(
    contract_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    contract = db.query(Contract).filter(
        Contract.id == contract_id
    ).first()

    if not contract:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contract not found"
        )

    return contract