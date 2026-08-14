from datetime import date

from pydantic import BaseModel


class ObligationCreate(BaseModel):
    contract_id: int
    title: str
    description: str
    due_date: date
    priority: str
    status: str
    assigned_to: int


class ObligationResponse(BaseModel):
    id: int
    contract_id: int
    title: str
    description: str
    due_date: date
    priority: str
    status: str
    assigned_to: int

    class Config:
        from_attributes = True