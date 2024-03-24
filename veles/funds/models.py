import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
    pass

class FundModel(Base):
    __tablename__ = "funds"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(unique=True)
    replenishment_bottom_limit: orm.Mapped[int | None]
    total_expense_percentage: orm.Mapped[float | None]
    capacity: orm.Mapped[int | None]

    orm.validates("replenishment_bottom_limit", "total_expense_percentage")
    def replenishment_validator(self, key, value):
        print(f"{key}: {value}")
        return value
