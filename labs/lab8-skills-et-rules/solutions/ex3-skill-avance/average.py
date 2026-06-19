"""Calculate average of numbers following TDD workflow.

This module demonstrates the Red-Green-Refactor cycle:
1. RED: Tests written first (in test_average.py)
2. GREEN: Minimal implementation to pass tests
3. REFACTOR: Improved code with documentation
"""


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    This function follows TDD principles:
    - Tests were written first
    - Implementation made tests pass
    - Code was refactored for clarity

    Args:
        numbers: List of numbers to average. Must not be empty.

    Returns:
        The arithmetic mean of the numbers.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> calculate_average([1.0, 2.0, 3.0])
        2.0
        >>> calculate_average([10.0])
        10.0
        >>> calculate_average([-1.0, 0.0, 1.0])
        0.0

    Notes:
        - Handles positive, negative, and mixed numbers
        - Maintains floating-point precision
        - Validates input before processing
    """
    # Step 2: GREEN - Validate input (make tests pass)
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")

    # Step 3: REFACTOR - Clean, readable implementation
    total = sum(numbers)
    count = len(numbers)
    return total / count


if __name__ == "__main__":
    # Demonstration of the function
    print("TDD Workflow Demonstration")
    print("=" * 50)

    # Example 1: Positive numbers
    test_data_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    result_1 = calculate_average(test_data_1)
    print(f"Average of {test_data_1}: {result_1}")

    # Example 2: Mixed numbers
    test_data_2 = [-10.0, 0.0, 10.0]
    result_2 = calculate_average(test_data_2)
    print(f"Average of {test_data_2}: {result_2}")

    # Example 3: Single number
    test_data_3 = [42.0]
    result_3 = calculate_average(test_data_3)
    print(f"Average of {test_data_3}: {result_3}")

    # Example 4: Error handling
    try:
        calculate_average([])
    except ValueError as e:
        print(f"Error with empty list: {e}")

# Made with Bob
