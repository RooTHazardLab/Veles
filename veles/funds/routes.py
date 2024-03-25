import fastapi
import database

import funds.models as models
import funds.schemas as schemas

router = fastapi.APIRouter(prefix='/funds', tags=["funds"])

@router.get("")
async def get_funds(
    db_session=fastapi.Depends(database.get_session)
) -> list[schemas.FundResponseSchema]:
    return [fund for fund in db_session.query(models.FundModel).all()]


@router.post("")
async def post_funds(
    fund: schemas.FundPostRequestSchema,
    db_session=fastapi.Depends(database.get_session)
):
    new_fund = models.FundModel(**fund.model_dump())

    db_session.add(new_fund)
    db_session.commit()

    return new_fund


@router.delete("/{fund_id}", status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def delete_funds(
    fund_id: int,
    db_session=fastapi.Depends(database.get_session)
):
    fund = db_session.query(models.FundModel).get(fund_id)

    db_session.delete(fund)
    db_session.commit()


@router.patch("/{fund_id}")
async def patch_funds(
    fund_id: int,
    fund: schemas.FundPatchRequestSchema,
    db_session=fastapi.Depends(database.get_session)
):
    fund_from_db = db_session.query(models.FundModel).get(fund_id)

    fund_from_db.replenishment_bottom_limit = fund.replenishment_bottom_limit
    fund_from_db.total_expense_percentage = fund.total_expense_percentage
    fund_from_db.capacity = fund.capacity

    db_session.commit()
