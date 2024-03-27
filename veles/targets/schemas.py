import pydantic

class TargetResponseSchema(pydantic.BaseModel):
    id: int
    name: str
    price: int
    priority: int
    fund_name: str


class TargetPostRequestSchema(pydantic.BaseModel):
    name: str
    price: int
    priority: int
    fund_name: str


class TargetPatchRequestSchema(pydantic.BaseModel):
    id: int
    price: int
    priority: int
    fund_name: str
