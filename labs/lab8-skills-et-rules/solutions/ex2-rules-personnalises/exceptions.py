"""Custom exceptions for the user service.

This module defines application-specific exceptions.
"""


class UserNotFoundException(Exception):
    """Raised when a user is not found in the repository.

    Attributes:
        user_id: The ID of the user that was not found.
        message: Explanation of the error.
    """

    def __init__(self, user_id: int) -> None:
        """Initialize the exception.

        Args:
            user_id: The ID of the user that was not found.
        """
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found"
        super().__init__(self.message)


class ValidationError(Exception):
    """Raised when input validation fails.

    Attributes:
        field: The field that failed validation.
        message: Explanation of the validation error.
    """

    def __init__(self, field: str, message: str) -> None:
        """Initialize the exception.

        Args:
            field: The field that failed validation.
            message: Explanation of the validation error.
        """
        self.field = field
        self.message = f"Validation error for '{field}': {message}"
        super().__init__(self.message)

# Made with Bob
