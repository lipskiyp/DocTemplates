"""
Database controller factory.
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import db_session
import app.controllers as controllers
import app.repositories as repositories


class ControllerFactory:
    """
    Database controller factory.
    """
    
    @staticmethod
    def get_template_controller(
        session: AsyncSession = Depends(db_session)
    ) -> controllers.TemplateController:
        """
        Returns Template database controller.
        """
        return controllers.TemplateController(
            repository=repositories.TemplateRepository(
                session=session
            )
        )
    

    @staticmethod
    def get_user_controller(
        session: AsyncSession = Depends(db_session)
    ) -> controllers.UserController:
        """
        Returns User database controller.
        """
        return controllers.UserController(
            repository=repositories.UserRepository(
                session=session
            )
        )