"""Repository layer for user data access.

This module implements the Repository pattern for user data management.
"""

import logging
from typing import Optional

from models import User
from exceptions import UserNotFoundException

logger = logging.getLogger(__name__)


class UserRepository:
    """Repository for managing user data persistence.

    This class follows the Repository pattern to abstract data access logic.
    """

    def __init__(self) -> None:
        """Initialize the repository with an in-memory storage."""
        self._users: dict[int, User] = {}
        self._next_id: int = 1
        logger.info("UserRepository initialized")

    def get_by_id(self, user_id: int) -> User:
        """Retrieve a user by their ID.

        Args:
            user_id: The unique identifier of the user.

        Returns:
            The User object if found.

        Raises:
            UserNotFoundException: If no user exists with the given ID.
        """
        logger.debug(f"Attempting to retrieve user with ID: {user_id}")

        user = self._users.get(user_id)
        if user is None:
            logger.warning(f"User with ID {user_id} not found")
            raise UserNotFoundException(user_id)

        logger.info(f"Successfully retrieved user with ID: {user_id}")
        return user

    def save(self, user: User) -> User:
        """Save a user to the repository.

        Args:
            user: The User object to save.

        Returns:
            The saved User object with an assigned ID if it was new.
        """
        if user.user_id == 0:
            user.user_id = self._next_id
            self._next_id += 1
            logger.info(f"Created new user with ID: {user.user_id}")
        else:
            logger.info(f"Updated user with ID: {user.user_id}")

        self._users[user.user_id] = user
        return user

    def delete(self, user_id: int) -> None:
        """Delete a user from the repository.

        Args:
            user_id: The unique identifier of the user to delete.

        Raises:
            UserNotFoundException: If no user exists with the given ID.
        """
        if user_id not in self._users:
            logger.warning(f"Cannot delete: User with ID {user_id} not found")
            raise UserNotFoundException(user_id)

        del self._users[user_id]
        logger.info(f"Deleted user with ID: {user_id}")

    def find_all(self) -> list[User]:
        """Retrieve all users from the repository.

        Returns:
            A list of all User objects.
        """
        logger.debug(f"Retrieving all users (count: {len(self._users)})")
        return list(self._users.values())

# Made with Bob
