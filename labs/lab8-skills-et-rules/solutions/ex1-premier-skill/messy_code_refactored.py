"""Refactored code following Python style guide.

This module demonstrates clean code practices with proper naming,
type hints, and documentation.
"""


def calculate_result(value_a: float, value_b: float, multiplier: float) -> float:
    """Calculate a result based on three values.

    The calculation follows the formula: ((a + b) * c) / 2

    Args:
        value_a: First value to add.
        value_b: Second value to add.
        multiplier: Value to multiply the sum by.

    Returns:
        The calculated result.

    Examples:
        >>> calculate_result(2.0, 3.0, 4.0)
        10.0
    """
    sum_values = value_a + value_b
    product = sum_values * multiplier
    result = product / 2
    return result


def process_positive_values(data: list[float]) -> list[float]:
    """Process a list of numbers, doubling positive values.

    Args:
        data: List of numbers to process.

    Returns:
        List containing doubled positive values from the input.

    Examples:
        >>> process_positive_values([1, -2, 3, 0, 5])
        [2, 6, 10]
    """
    return [value * 2 for value in data if value > 0]


class User:
    """Represents a user with name, email, and age.

    Attributes:
        name: The user's full name.
        email: The user's email address.
        age: The user's age in years.
    """

    def __init__(self, name: str, email: str, age: int) -> None:
        """Initialize a User instance.

        Args:
            name: The user's full name.
            email: The user's email address.
            age: The user's age in years.
        """
        self.name = name
        self.email = email
        self.age = age

    def get_info(self) -> str:
        """Get formatted user information.

        Returns:
            A string containing the user's name, email, and age.

        Examples:
            >>> user = User("John Doe", "john@example.com", 30)
            >>> user.get_info()
            'John Doe john@example.com 30'
        """
        return f"{self.name} {self.email} {self.age}"

    def __repr__(self) -> str:
        """Return a string representation of the User.

        Returns:
            A string representation suitable for debugging.
        """
        return f"User(name='{self.name}', email='{self.email}', age={self.age})"


if __name__ == "__main__":
    # Test calculate_result
    result = calculate_result(2.0, 3.0, 4.0)
    print(f"Calculate result: {result}")

    # Test process_positive_values
    test_data = [1, -2, 3, 0, 5, -7, 10]
    processed = process_positive_values(test_data)
    print(f"Processed values: {processed}")

    # Test User class
    user = User("Alice Smith", "alice@example.com", 28)
    print(f"User info: {user.get_info()}")
    print(f"User repr: {repr(user)}")

# Made with Bob
