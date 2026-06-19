"""Tests for the calculate_average function following TDD workflow.

This module demonstrates the Red-Green-Refactor cycle.
"""

import pytest
from average import calculate_average


# Step 1: RED - Write failing tests
def test_calculate_average_with_positive_numbers() -> None:
    """Test average calculation with positive numbers."""
    result = calculate_average([1.0, 2.0, 3.0])
    assert result == 2.0


def test_calculate_average_with_single_number() -> None:
    """Test average calculation with a single number."""
    result = calculate_average([5.0])
    assert result == 5.0


def test_calculate_average_with_negative_numbers() -> None:
    """Test average calculation with negative numbers."""
    result = calculate_average([-1.0, -2.0, -3.0])
    assert result == -2.0


def test_calculate_average_with_mixed_numbers() -> None:
    """Test average calculation with mixed positive and negative numbers."""
    result = calculate_average([-10.0, 0.0, 10.0])
    assert result == 0.0


def test_calculate_average_with_floats() -> None:
    """Test average calculation with floating point numbers."""
    result = calculate_average([1.5, 2.5, 3.5])
    assert result == 2.5


def test_calculate_average_empty_list_raises_error() -> None:
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])


def test_calculate_average_with_large_numbers() -> None:
    """Test average calculation with large numbers."""
    result = calculate_average([1000000.0, 2000000.0, 3000000.0])
    assert result == 2000000.0


def test_calculate_average_precision() -> None:
    """Test average calculation maintains precision."""
    result = calculate_average([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == 3.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Made with Bob
