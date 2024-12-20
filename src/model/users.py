from sqlalchemy import String, Integer, ForeignKey, JSON, BigInteger, UniqueConstraint, Float
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, time

from src.database import Base, int_pk


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    state: Mapped[str] = mapped_column(String, nullable=True)
    state_data: Mapped[dict] = mapped_column(JSON, nullable=True)

    root: Mapped["RootUser"] = relationship(back_populates="user", uselist=False)
    bot: Mapped["Bot"] = relationship(back_populates="user", uselist=False)
    lead: Mapped["LeadUser"] = relationship(back_populates="user", uselist=False)

    @hybrid_property
    def full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.user_id}, username={self.username!r})"  # , role={self.role!r}

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class RootUser(Base):
    __tablename__ = "root_users"
    admin_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id"))

    user: Mapped["User"] = relationship(back_populates="root", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.admin_id}, user_id={self.user_id!r})"  # , role={self.role!r}

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "admin_id": self.admin_id,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Bot(Base):
    __tablename__ = "bots"

    bot_id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id"))
    phone_number: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship(back_populates="bot", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.bot_id}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "bot_id": self.bot_id,
            "user_id": self.user_id,
        }


class LeadUser(Base):
    __tablename__ = "lead_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id"))
    lang: Mapped[str] = mapped_column(String, nullable=True)

    user: Mapped["User"] = relationship(back_populates="lead", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }


class FoodOrder(Base):
    __tablename__ = "food_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    total_price: Mapped[float] = mapped_column(Float)
    order_type: Mapped[str] = mapped_column(String, nullable=True)

    order_items: Mapped["FoodOrderItem"] = relationship(back_populates="order", cascade="all, delete-orphan")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, total_price={self.total_price})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "total_price": self.total_price,
            "created_at": self.created_at,
        }


class FoodOrderItem(Base):
    __tablename__ = "food_order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("food_orders.id"))
    product_number: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)

    order: Mapped["FoodOrder"] = relationship(back_populates="order_items", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, order_id={self.order_id}, product_number={self.product_number}, quantity={self.quantity})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_number": self.product_number,
            "quantity": self.quantity,
        }
