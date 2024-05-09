"""
Template database controller.
"""

from app.models import Template
from app.repositories import TemplateRepository
from core.controllers import BaseController


class TemplateController(BaseController):
    """
    Template database controller.
    """

    def __init__(
        self, repository: TemplateRepository
    ) -> None:
        super().__init__(model=Template, repository=repository)
        