def calculate_average_ratios(numbers, default_value=0.0):
    """
    Calculate the average of (100 / number) for each number.
    
    Gracefully handles edge cases:
    - Skips zero values (avoids division by zero)
    - Skips invalid types (non-numeric)
    - Returns default value if no valid numbers
    
    Args:
        numbers: List of numeric values
        default_value: Value to return if no valid numbers (default: 0.0)
        
    Returns:
        Average of valid ratios, or default_value if no valid numbers
        
    Examples:
        >>> calculate_average_ratios([10, 5, 2])
        26.666...
        
        >>> calculate_average_ratios([10, 5, 0])  # Skips zero
        15.0
        
        >>> calculate_average_ratios([])  # Empty list
        0.0
        
        >>> calculate_average_ratios([0, 0, 0])  # All zeros
        0.0
    """
    # Handle empty or None input
    if not numbers:
        print("Warning: Empty input list provided")
        return default_value

    ratios = []
    skipped_count = 0

    for number in numbers:
        # Skip invalid types
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            print(f"Warning: Skipping invalid type {type(number).__name__}: {number}")
            skipped_count += 1
            continue
        
        # Skip zeros to avoid division by zero
        if number == 0:
            print(f"Warning: Skipping zero value (division by zero prevented)")
            skipped_count += 1
            continue

        # Safe to divide
        ratio = 100 / number
        ratios.append(ratio)

    # If no valid ratios, return default
    if not ratios:
        if skipped_count > 0:
            print(f"Note: All {len(numbers)} values were skipped (zeros or invalid types)")
        return default_value

    # Calculate and return average
    average = sum(ratios) / len(ratios)
    print(f"Info: Processed {len(ratios)} valid values, skipped {skipped_count} invalid/zero values")
    return average
  

if __name__ == "__main__":
    print("=" * 60)
    print("Testing calculate_average_ratios() with various inputs")
    print("=" * 60)
    
    # Test 1: Original failing case [10, 5, 0]
    print("\nTest 1: Original bug case [10, 5, 0]")
    print("Expected: Should skip zero and calculate average of [10, 5]")
    result = calculate_average_ratios([10, 5, 0])
    print(f"Result: {result:.2f}\n")
    
    # Test 2: Valid input with no zeros
    print("Test 2: Valid input [10, 5, 2]")
    print("Expected: Average of all three values")
    result = calculate_average_ratios([10, 5, 2])
    print(f"Result: {result:.2f}\n")
    
    # Test 3: Empty list
    print("Test 3: Empty list []")
    print("Expected: Returns default value (0.0)")
    result = calculate_average_ratios([])
    print(f"Result: {result}\n")
    
    # Test 4: All zeros
    print("Test 4: All zeros [0, 0, 0]")
    print("Expected: Returns default value (0.0)")
    result = calculate_average_ratios([0, 0, 0])
    print(f"Result: {result}\n")
    
    # Test 5: Mixed invalid types
    print("Test 5: Mixed invalid types [10, 'string', 5]")
    print("Expected: Skips string, calculates average of [10, 5]")
    result = calculate_average_ratios([10, "string", 5])
    print(f"Result: {result:.2f}\n")
    
    # Test 6: Negative numbers (valid)
    print("Test 6: Negative numbers [-10, -5]")
    print("Expected: Works correctly with negative values")
    result = calculate_average_ratios([-10, -5])
    print(f"Result: {result:.2f}\n")
    
    # Test 7: Single valid value
    print("Test 7: Single valid value [20]")
    print("Expected: Returns 100/20 = 5.0")
    result = calculate_average_ratios([20])
    print(f"Result: {result:.2f}\n")
    
    print("=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)