from datetime import datetime
from typing import Annotated

from sqlalchemy import func, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, sessionmaker

import src.settings as stg

int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_false = Annotated[str, mapped_column(nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


def get_db_url():
    return f"postgresql://{stg.DB_USER}:{stg.DB_PASSWORD}@{stg.DB_HOST}:{stg.DB_PORT}/{stg.DB_NAME}"


engine = create_engine(get_db_url())
session_maker = sessionmaker(engine, expire_on_commit=False)
