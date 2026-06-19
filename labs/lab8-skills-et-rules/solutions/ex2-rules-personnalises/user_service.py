"""Business logic layer for user management.

This module implements the service layer following the layered architecture.
"""

import logging
from typing import Optional

from models import User
from user_repository import UserRepository
from exceptions import UserNotFoundException, ValidationError

logger = logging.getLogger(__name__)


class UserService:
    """Service class for user business logic.

    This class implements the business logic layer and coordinates
    between the presentation and data layers.
    """

    def __init__(self, repository: UserRepository) -> None:
        """Initialize the service with a repository.

        Args:
            repository: The UserRepository instance for data access.
        """
        self._repository = repository
        logger.info("UserService initialized")

    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve a user by their ID.

        Args:
            user_id: The unique identifier of the user.

        Returns:
            The User object if found.

        Raises:
            ValidationError: If the user_id is invalid (not positive).
            UserNotFoundException: If no user exists with the given ID.
        """
        logger.info(f"Getting user by ID: {user_id}")

        # Validate input
        if user_id <= 0:
            logger.error(f"Invalid user_id: {user_id}")
            raise ValidationError("user_id", "User ID must be a positive integer")

        try:
            user = self._repository.get_by_id(user_id)
            logger.info(f"Successfully retrieved user: {user.name}")
            return user
        except UserNotFoundException as e:
            logger.error(f"User not found: {e.message}")
            raise

    def create_user(self, name: str, email: str, age: int) -> User:
        """Create a new user.

        Args:
            name: The user's full name.
            email: The user's email address.
            age: The user's age in years.

        Returns:
            The created User object.

        Raises:
            ValidationError: If any input is invalid.
        """
        logger.info(f"Creating new user: {name}")

        # Validate inputs
        self._validate_user_data(name, email, age)

        # Create and save user
        user = User(user_id=0, name=name, email=email, age=age)
        saved_user = self._repository.save(user)

        logger.info(f"User created successfully with ID: {saved_user.user_id}")
        return saved_user

    def update_user(
        self, user_id: int, name: str, email: str, age: int
    ) -> User:
        """Update an existing user.

        Args:
            user_id: The unique identifier of the user to update.
            name: The user's new full name.
            email: The user's new email address.
            age: The user's new age in years.

        Returns:
            The updated User object.

        Raises:
            ValidationError: If any input is invalid.
            UserNotFoundException: If no user exists with the given ID.
        """
        logger.info(f"Updating user with ID: {user_id}")

        # Validate user exists
        existing_user = self.get_user_by_id(user_id)

        # Validate new data
        self._validate_user_data(name, email, age)

        # Update user
        updated_user = User(user_id=user_id, name=name, email=email, age=age)
        saved_user = self._repository.save(updated_user)

        logger.info(f"User updated successfully: {saved_user.name}")
        return saved_user

    def delete_user(self, user_id: int) -> None:
        """Delete a user.

        Args:
            user_id: The unique identifier of the user to delete.

        Raises:
            ValidationError: If the user_id is invalid.
            UserNotFoundException: If no user exists with the given ID.
        """
        logger.info(f"Deleting user with ID: {user_id}")

        # Validate input
        if user_id <= 0:
            logger.error(f"Invalid user_id: {user_id}")
            raise ValidationError("user_id", "User ID must be a positive integer")

        self._repository.delete(user_id)
        logger.info(f"User deleted successfully: {user_id}")

    def list_all_users(self) -> list[User]:
        """Retrieve all users.

        Returns:
            A list of all User objects.
        """
        logger.info("Listing all users")
        users = self._repository.find_all()
        logger.info(f"Retrieved {len(users)} users")
        return users

    def _validate_user_data(self, name: str, email: str, age: int) -> None:
        """Validate user data.

        Args:
            name: The user's full name.
            email: The user's email address.
            age: The user's age in years.

        Raises:
            ValidationError: If any validation fails.
        """
        if not name or not name.strip():
            raise ValidationError("name", "Name cannot be empty")

        if not email or "@" not in email:
            raise ValidationError("email", "Invalid email format")

        if age < 0 or age > 150:
            raise ValidationError("age", "Age must be between 0 and 150")

# Made with Bob
