import pydantic

class FundResponseSchema(pydantic.BaseModel):
    id: int
    name: str
    replenishment_bottom_limit: int | None
    total_expense_percentage: float | None
    capacity: int | None


class FundRequestSchema(pydantic.BaseModel):
    name: str
    replenishment_bottom_limit: int | None
    total_expense_percentage: float | None
    capacity: int | None
