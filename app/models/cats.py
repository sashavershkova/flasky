from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    breed: Mapped[str]


# cats = [
#     Cat(1, "Whiskers", "gray", "British Shorthair"),
#     Cat(2, "Luna", "black", "Bombay"),
#     Cat(3, "Simba", "orange", "Maine Coon"),
#     Cat(4, "Mochi", "white", "Persian"),
#     Cat(5, "Shadow", "tabby", "American Shorthair")
# ]

