"""
Template SQLAlchemy ORM model.
"""

from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from core.models import CommonBase


class Template(CommonBase):
    """
    Template ORM model.
    """
    __tablename__ = "templates"

    name: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    permissions: Mapped[dict[str, str]] = mapped_column(
        JSON(),
        nullable=True,
    )
