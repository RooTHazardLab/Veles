import fastapi
import database

import funds.models as funds_models

import targets.models as models
import targets.schemas as schemas

router = fastapi.APIRouter(prefix='/targets', tags=["targets"])

@router.get("")
async def get_targets(
    db_session=fastapi.Depends(database.get_session)
) -> list[schemas.TargetResponseSchema]:
    res = []

    for target in db_session.query(models.TargetModel).all():
        res.append(schemas.TargetResponseSchema(
            target.id, target.name, target.price, target.fund.name
        ))

    return res


@router.post("")
async def post_targets(
    target: schemas.TargetPostRequestSchema,
    db_session=fastapi.Depends(database.get_session)
):
    fund_from_db = db_session.query(
        funds_models.FundModel
    ).filter_by(name=target.fund_name).first()

    if fund_from_db is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Fund {target.fund_name} not found"
        )

    new_target = models.TargetModel(
        name=target.name, price=target.price, fund=fund_from_db
    )

    db_session.add(new_target)
    db_session.commit()

    return new_target


@router.delete("/{target_id}", status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def delete_funds(
    target_id: int,
    db_session=fastapi.Depends(database.get_session)
):
    target = db_session.query(models.TargetModel).get(target_id)

    db_session.delete(target)
    db_session.commit()


@router.patch("/{target_id}")
async def patch_funds(
    target_id: int,
    target: schemas.TargetPatchRequestSchema,
    db_session=fastapi.Depends(database.get_session)
):
    target_from_db = db_session.query(models.TargetModel).get(target_id)

    fund_from_db = db_session.query(
        funds_models.FundModel
    ).filter_by(name=target.fund_name).first()

    if fund_from_db is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Fund {target.fund_name} not found"
        )

    target_from_db.price = target.price
    target_from_db.priority = target.priority
    target_from_db.fund = fund_from_db

    db_session.commit()
