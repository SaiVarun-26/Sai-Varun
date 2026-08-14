from datetime import date

from pydantic import BaseModel


class ContractCreate(BaseModel):
    contract_number: str
    vendor_name: str
    start_date: date
    end_date: date
    contract_value: float
    status: str
    created_by: int


class ContractResponse(BaseModel):
    id: int
    contract_number: str
    vendor_name: str
    start_date: date
    end_date: date
    contract_value: float
    status: str
    created_by: int

    class Config:
        from_attributes = True