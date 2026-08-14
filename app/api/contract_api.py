from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract
from app.schemas.contract_schema import ContractCreate, ContractResponse


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
    db: Session = Depends(get_db)
):
    contract = Contract(
        contract_number=contract_data.contract_number,
        vendor_name=contract_data.vendor_name,
        start_date=contract_data.start_date,
        end_date=contract_data.end_date,
        contract_value=contract_data.contract_value,
        status=contract_data.status,
        created_by=contract_data.created_by
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