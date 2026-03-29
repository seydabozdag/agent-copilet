"""Module for solving quadratic equations."""

import math
from typing import Optional, Tuple
from quadratic_solver import solve_quadratic_equation

def solve_quadratic_equation(
    a: float, b: float, c: float
) -> Optional[Tuple[float, float]]:
    """Solve a quadratic equation of the form ax² + bx + c = 0.
    
    Uses the quadratic formula: x = (-b ± √(b² - 4ac)) / 2a
    
    Args:
        a: Coefficient of x²
        b: Coefficient of x
        c: Constant term
        
    Returns:
        Tuple of two solutions (x1, x2) if real solutions exist,
        None if discriminant is negative (complex solutions)
        
    Raises:
        ValueError: If a is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero. Use linear equation solver.")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None  # No real solutions
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    
    return (x1, x2)


# Example usage
if __name__ == "__main__":
    result = solve_quadratic_equation(1, -5, 6)  # x² - 5x + 6 = 0
    if result:
        print(f"Solutions: x1 = {result[0]}, x2 = {result[1]}")
    else:
        print("No real solutions exist")
