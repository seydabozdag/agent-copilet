#!/usr/bin/env python3
"""Demo script showing the fix in action.

Demonstrates how the original code crashes and the fixed code handles it gracefully.
"""

from calculator import calculate_average_ratios


def demo_original_bug():
    """Show what WOULD happen with the original code (simulated)."""
    print("=" * 70)
    print("ORIGINAL BUGGY CODE - What would happen:")
    print("=" * 70)
    print("\nCode: average_ratios([10, 5, 0])")
    print("\nExecution trace:")
    print("  i=0: 100 / 10 = 10.0 ✓")
    print("  i=1: 100 / 5  = 20.0 ✓")
    print("  i=2: 100 / 0  = ❌ CRASH!")
    print("\nError: ZeroDivisionError: division by zero")
    print("Result: Program crashes, no output returned\n")


def demo_fixed_code():
    """Show how the fixed code handles various scenarios."""
    print("=" * 70)
    print("FIXED CODE - Handles edge cases gracefully:")
    print("=" * 70)

    # Test 1: Valid input
    print("\n1️⃣  Valid input [10, 5, 2]:")
    try:
        result = calculate_average_ratios([10, 5, 2])
        print(f"   ✅ Success: Average ratio = {result:.2f}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    # Test 2: THE ORIGINAL BUG CASE
    print("\n2️⃣  Original bug case [10, 5, 0]:")
    try:
        result = calculate_average_ratios([10, 5, 0])
        print(f"   Result: {result}")
    except ValueError as e:
        print(f"   ✅ Caught gracefully: {e}")

    # Test 3: Single zero
    print("\n3️⃣  Single zero [0]:")
    try:
        result = calculate_average_ratios([0])
        print(f"   Result: {result}")
    except ValueError as e:
        print(f"   ✅ Caught gracefully: {e}")

    # Test 4: Empty list
    print("\n4️⃣  Empty list []:")
    try:
        result = calculate_average_ratios([])
        print(f"   Result: {result}")
    except ValueError as e:
        print(f"   ✅ Caught gracefully: {e}")

    # Test 5: Invalid type
    print("\n5️⃣  Invalid type [10, '5', 2]:")
    try:
        result = calculate_average_ratios([10, "5", 2])
        print(f"   Result: {result}")
    except TypeError as e:
        print(f"   ✅ Caught gracefully: {e}")

    # Test 6: Negative numbers (valid)
    print("\n6️⃣  Negative numbers [-10, -5]:")
    try:
        result = calculate_average_ratios([-10, -5])
        print(f"   ✅ Success: Average ratio = {result:.2f}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    # Test 7: Boolean rejection
    print("\n7️⃣  Boolean input [True]:")
    try:
        result = calculate_average_ratios([True])
        print(f"   Result: {result}")
    except TypeError as e:
        print(f"   ✅ Caught gracefully: {e}")


def show_improvements():
    """Display the improvements made."""
    print("\n" + "=" * 70)
    print("IMPROVEMENTS SUMMARY:")
    print("=" * 70)
    
    improvements = [
        ("Division by zero", "❌ Crashes", "✅ Raises ValueError with message"),
        ("Type validation", "❌ None", "✅ Rejects invalid types"),
        ("Empty input", "❌ Divide by zero error", "✅ Raises clear ValueError"),
        ("Documentation", "❌ Minimal", "✅ Full docstring + type hints"),
        ("Error messages", "❌ Cryptic", "✅ Descriptive and helpful"),
        ("Negative numbers", "❌ Undefined", "✅ Works correctly"),
    ]
    
    for feature, before, after in improvements:
        print(f"\n{feature}:")
        print(f"  Before: {before}")
        print(f"  After:  {after}")


if __name__ == "__main__":
    print("\n")
    demo_original_bug()
    demo_fixed_code()
    show_improvements()
    print("\n" + "=" * 70)
    print("✅ All edge cases handled properly!")
    print("=" * 70 + "\n")
