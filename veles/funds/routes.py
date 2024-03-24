import fastapi
import database

import funds.models as models
import funds.schemas as schemas

router = fastapi.APIRouter(prefix='/funds', tags=["funds"])

@router.get("")
async def get_funds(
    db_session=fastapi.Depends(database.get_session)
) -> list[schemas.FundResponseSchema]:
    res = [fund for fund in db_session.query(models.FundModel).all()]
    print(res)
    return res


@router.post("")
async def post_funds(
    fund: schemas.FundRequestSchema,
    db_session=fastapi.Depends(database.get_session)
):
    new_fund = models.FundModel(**fund.model_dump())

    db_session.add(new_fund)
    db_session.commit()

    return new_fund
