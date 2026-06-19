"""Test module for calculate_average function.

This module demonstrates the use of the python-style skill.
"""


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers to average.

    Returns:
        The average value.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> calculate_average([1.0, 2.0, 3.0])
        2.0
        >>> calculate_average([10.0, 20.0])
        15.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Test examples
    test_data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_average(test_data)
    print(f"Average of {test_data}: {result}")

    # Test with different data
    test_data_2 = [10.5, 20.3, 15.7]
    result_2 = calculate_average(test_data_2)
    print(f"Average of {test_data_2}: {result_2}")

# Made with Bob
