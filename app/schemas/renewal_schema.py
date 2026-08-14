from datetime import date

from pydantic import BaseModel


class RenewalCreate(BaseModel):
    contract_id: int
    renewal_date: date
    reminder_days: int
    status: str


class RenewalResponse(BaseModel):
    id: int
    contract_id: int
    renewal_date: date
    reminder_days: int
    status: str

    class Config:
        from_attributes = True