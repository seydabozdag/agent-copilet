"""Unit tests for the calculate_average_ratios function.

Verifies error handling, edge cases, and correct calculations.
"""

import unittest
from calculator import calculate_average_ratios


class TestCalculateAverageRatios(unittest.TestCase):
    """Test suite for calculate_average_ratios function."""

    # ==================== HAPPY PATH TESTS ====================
    
    def test_valid_calculation_basic(self):
        """Test basic calculation with valid inputs."""
        result = calculate_average_ratios([10, 5])
        expected = (100/10 + 100/5) / 2  # (10 + 20) / 2 = 15
        self.assertAlmostEqual(result, expected, places=5)

    def test_valid_calculation_multiple_values(self):
        """Test calculation with multiple values."""
        result = calculate_average_ratios([10, 5, 2])
        # Ratios: 100/10=10, 100/5=20, 100/2=50
        # Average: (10 + 20 + 50) / 3 = 26.666...
        expected = (10 + 20 + 50) / 3
        self.assertAlmostEqual(result, expected, places=5)

    def test_single_value(self):
        """Test with a single value."""
        result = calculate_average_ratios([10])
        expected = 100 / 10  # = 10
        self.assertAlmostEqual(result, expected, places=5)

    def test_negative_numbers(self):
        """Test with negative numbers (valid edge case)."""
        result = calculate_average_ratios([-10, -5])
        # Ratios: 100/-10=-10, 100/-5=-20
        # Average: (-10 + -20) / 2 = -15
        expected = (-10 + -20) / 2
        self.assertAlmostEqual(result, expected, places=5)

    def test_float_inputs(self):
        """Test with floating point inputs."""
        result = calculate_average_ratios([4.0, 2.0])
        # Ratios: 100/4=25, 100/2=50
        # Average: (25 + 50) / 2 = 37.5
        expected = 37.5
        self.assertAlmostEqual(result, expected, places=5)

    def test_very_small_number(self):
        """Test with very small (but non-zero) number."""
        result = calculate_average_ratios([0.001])
        expected = 100 / 0.001  # = 100000
        self.assertAlmostEqual(result, expected, places=2)

    # ==================== ERROR HANDLING TESTS ====================

    def test_division_by_zero_single(self):
        """Test that division by zero is caught."""
        with self.assertRaises(ValueError) as context:
            calculate_average_ratios([0])
        
        self.assertIn("Division by zero", str(context.exception))

    def test_division_by_zero_in_middle(self):
        """Test that zero in the middle of list is caught.
        
        This is the exact scenario from the bug report: [10, 5, 0]
        """
        with self.assertRaises(ValueError) as context:
            calculate_average_ratios([10, 5, 0])  # ❌ Original bug
        
        self.assertIn("Division by zero", str(context.exception))

    def test_multiple_zeros(self):
        """Test list with multiple zeros."""
        with self.assertRaises(ValueError):
            calculate_average_ratios([0, 0, 0])

    def test_empty_list(self):
        """Test that empty list is handled gracefully."""
        with self.assertRaises(ValueError) as context:
            calculate_average_ratios([])
        
        self.assertIn("empty", str(context.exception).lower())

    # ==================== TYPE VALIDATION TESTS ====================

    def test_boolean_input_rejected(self):
        """Test that booleans are rejected (not treated as 0/1)."""
        with self.assertRaises(TypeError):
            calculate_average_ratios([True])
        
        with self.assertRaises(TypeError):
            calculate_average_ratios([False])

    def test_string_input_rejected(self):
        """Test that string inputs are rejected."""
        with self.assertRaises(TypeError):
            calculate_average_ratios(["10"])

    def test_none_input_rejected(self):
        """Test that None is rejected."""
        with self.assertRaises(TypeError):
            calculate_average_ratios([None])

    def test_mixed_valid_and_invalid_types(self):
        """Test list with mixed types."""
        with self.assertRaises(TypeError):
            calculate_average_ratios([10, "5", 2])

    def test_integer_input_accepted(self):
        """Test that integers are accepted."""
        result = calculate_average_ratios([10, 5])
        self.assertIsInstance(result, float)

    # ==================== PRECISION AND EDGE CASES ====================

    def test_result_is_float(self):
        """Test that result is always a float."""
        result = calculate_average_ratios([10])
        self.assertIsInstance(result, float)

    def test_large_numbers(self):
        """Test with very large numbers."""
        result = calculate_average_ratios([1_000_000, 2_000_000])
        expected = (100/1_000_000 + 100/2_000_000) / 2
        self.assertAlmostEqual(result, expected, places=10)

    def test_precision_maintained(self):
        """Test that floating point precision is maintained."""
        result = calculate_average_ratios([3])
        expected = 100 / 3
        self.assertAlmostEqual(result, expected, places=10)


class TestRobustnessScenarios(unittest.TestCase):
    """Additional robustness tests for real-world scenarios."""

    def test_academic_example(self):
        """Test the original failing example: [10, 5, 0]."""
        # This should NOT crash anymore - it should raise ValueError
        with self.assertRaises(ValueError):
            calculate_average_ratios([10, 5, 0])

    def test_percentage_calculations(self):
        """Test realistic percentage calculation scenario."""
        # Simulating marks/scores
        scores = [85.5, 90.0, 78.25]
        result = calculate_average_ratios(scores)
        expected = (100/85.5 + 100/90.0 + 100/78.25) / 3
        self.assertAlmostEqual(result, expected, places=5)

    def test_conversion_factors(self):
        """Test realistic unit conversion scenario."""
        # Converting from one unit to another
        measurements = [2.0, 4.0, 5.0]
        result = calculate_average_ratios(measurements)
        expected = (100/2 + 100/4 + 100/5) / 3  # (50 + 25 + 20) / 3
        self.assertAlmostEqual(result, expected, places=5)


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
