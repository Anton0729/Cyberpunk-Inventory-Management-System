from sqlalchemy import Column, Integer, String, Boolean, Text, Float, Enum
import enum
from .database import Base


# Define the Enum for the category choices
class CategoryEnum(enum.Enum):
    WEAPON = "Weapon"
    CYBERNETIC = "Cybernetic"
    GADGET = "Gadget"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(Text, nullable=True)
    category = Column(Enum(CategoryEnum), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
