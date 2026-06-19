"""Data models for the user service.

This module defines the domain models used throughout the application.
"""

from dataclasses import dataclass


@dataclass
class User:
    """Represents a user in the system.

    Attributes:
        user_id: Unique identifier for the user.
        name: The user's full name.
        email: The user's email address.
        age: The user's age in years.
    """

    user_id: int
    name: str
    email: str
    age: int

# Made with Bob
