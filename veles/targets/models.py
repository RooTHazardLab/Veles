import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
    pass

class TargetModel(Base):
    __tablename__ = "targets"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column(unique=True)
    price: orm.Mapped[int]
    priority: orm.Mapped[int]
    fund_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey("funds.id", ondelete="CASCADE")
    )
