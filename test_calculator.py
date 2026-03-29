import pytest
from calculator import calculate_average_ratios


def test_valid_input():
    result = calculate_average_ratios([10, 5, 2])
    assert result == pytest.approx((10 + 20 + 50) / 3)


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average_ratios([])


def test_zero_in_list():
    with pytest.raises(ValueError):
        calculate_average_ratios([10, 0, 5])


def test_invalid_type_string():
    with pytest.raises(TypeError):
        calculate_average_ratios([10, "a", 5])


def test_invalid_type_bool():
    with pytest.raises(TypeError):
        calculate_average_ratios([True, 5])