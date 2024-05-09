"""
Template SQLAlchemy database repository.
"""

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Template
from core.repositories import BaseRepository


class TemplateRepository(BaseRepository):
    """
    Template SQLAlchemy database repository.
    """
    
    def __init__(
        self, session: AsyncSession
    ) -> None:
        super().__init__(model=Template, session=session)
