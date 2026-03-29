import math
from typing import Optional, Tuple


def solve_quadratic_equation(
    a: float, b: float, c: float
) -> Optional[Tuple[float, float]]:
    """Solve a quadratic equation of the form ax² + bx + c = 0."""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Coefficient 'a' must be numeric")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Coefficient 'b' must be numeric")

    if not isinstance(c, (int, float)) or isinstance(c, bool):
        raise TypeError("Coefficient 'c' must be numeric")

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None

    sqrt_discriminant = math.sqrt(discriminant)

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2


if __name__ == "__main__":
    result = solve_quadratic_equation(1, -5, 6)

    if result:
        x1, x2 = result
        print(f"x1 = {x1}, x2 = {x2}")
    else:
        print("No real solutions")