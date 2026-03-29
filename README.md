# 🎓 Python Module Learning Sandbox

A comprehensive educational project demonstrating **clean code practices**, **secure programming**, and **error handling** in Python.

---

## 📌 Project Overview

This sandbox contains multiple Python modules that serve as **learning examples** for:

- ✅ **Clean Code Principles** - Readable, modular, well-documented code
- ✅ **Security Best Practices** - Secure credential handling, safe logging
- ✅ **Error Handling** - Robust input validation, meaningful error messages
- ✅ **Testing** - Comprehensive unit tests with edge case coverage
- ✅ **Documentation** - Type hints, docstrings, and README guides

### Project Structure

```
mcp-student-sandbox/
├── calculator.py                    # Calculator with error handling
├── spaghetti_logic.py              # Data processing with secure logging
├── quadratic_solver.py             # Quadratic equation solver
├── secret_leak.py                  # AWS credential management (secure)
├── demo.py                         # Interactive demonstration
├── test_failing_calculator.py      # Comprehensive unit tests (21 tests)
├── README.md                       # This file
├── SECURITY_AUDIT.md              # Detailed security analysis
└── .logs/                          # Secure log directory (auto-created)
```

---

## 📚 Module Guide

### 1️⃣ **calculator.py** - Average Ratio Calculator

**What it does:** Calculates the average of ratio values (100 divided by each number).

**Why it matters:** Demonstrates proper error handling for edge cases like division by zero.

#### Function Signature:

```python
def calculate_average_ratios(numbers: List[float]) -> float:
    """
    Calculate average of (100 / number) for each number.

    Args:
        numbers: List of non-zero numeric values

    Returns:
        Average of all ratios

    Raises:
        ValueError: If empty, contains zero
        TypeError: If non-numeric values provided
    """
```

#### Usage Example:

```python
from calculator import calculate_average_ratios

# Valid input
result = calculate_average_ratios([10, 5, 2])
print(f"Average ratio: {result:.2f}")  # Output: 26.67

# Handles errors gracefully
try:
    result = calculate_average_ratios([10, 5, 0])  # Contains zero!
except ValueError as e:
    print(f"Error: {e}")  # Error: Division by zero encountered...
```

#### Key Features:

- ✅ Input validation (checks for empty list, zeros, invalid types)
- ✅ Type hints for clarity (`List[float] -> float`)
- ✅ Clear error messages explaining the problem
- ✅ Comprehensive docstrings

#### Common Mistakes Prevented:

| Problem                     | Solution                         |
| --------------------------- | -------------------------------- |
| Crashes on zero             | Added zero-check before division |
| Accepts booleans as numbers | Explicitly rejects `bool` type   |
| Vague error messages        | Descriptive messages explain why |
| No documentation            | Full docstrings and type hints   |

---

### 2️⃣ **spaghetti_logic.py** - Data Processing Pipeline

**What it does:** Processes a list of numeric values by applying a multiplier and logs results securely.

**Why it matters:** Demonstrates modular design, separation of concerns, and secure logging with rotation.

#### Key Functions:

```python
def apply_multiplier(value: float, multiplier: float = 1.15) -> float:
    """Apply a multiplier to a single value."""

def format_currency(value: float) -> str:
    """Format value as a readable string with 2 decimal places."""

def process_values(values: List[float], multiplier: float = 1.15) -> List[float]:
    """Core processing logic (pure function, no side effects)."""

def display_results(values: List[float]) -> None:
    """Print formatted results to console."""

def log_results(values: List[float]) -> None:
    """Log results to secured rotating file."""
```

#### Usage Example:

```python
from spaghetti_logic import process_values, display_results, log_results

# Process data
data = [10, 20, 30]
results = process_values(data, multiplier=1.15)

# Display and log
display_results(results)  # Prints formatted output
log_results(results)      # Writes to .logs/process.log

# Output in terminal:
# Total: 11.50
# Total: 23.00
# Total: 34.50
```

#### Secure Logging Features:

- 🔒 **Automatic Directory Creation** - Creates `.logs/` with owner-only permissions (mode 0o700)
- 🔄 **Log Rotation** - New file created at 5MB to prevent disk bloat
- 📝 **Rich Formatting** - Timestamp, logger name, severity level
- 🛡️ **No Sensitive Data** - Credentials never logged

**Log file example:**

```
2026-03-29 16:24:41,068 - __main__ - INFO - Processed values: [11.5, 23.0, 34.5]
```

#### Design Principles Demonstrated:

| Principle                  | Benefit                                        |
| -------------------------- | ---------------------------------------------- |
| **Single Responsibility**  | Each function does ONE thing                   |
| **Pure Functions**         | `process_values()` has no side effects         |
| **Separation of Concerns** | I/O separated from business logic              |
| **DRY**                    | Reusable validation in `_validate_*` functions |

---

### 3️⃣ **quadratic_solver.py** - Quadratic Equation Solver

**What it does:** Solves quadratic equations of the form `ax² + bx + c = 0` using the quadratic formula.

**Why it matters:** Demonstrates mathematical problem-solving with complete error handling and input validation.

#### The Quadratic Formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### Function Signature:

```python
def solve_quadratic_equation(
    a: float, b: float, c: float
) -> Optional[Tuple[float, float]]:
    """
    Solve ax² + bx + c = 0.

    Args:
        a, b, c: Equation coefficients (must be numeric)

    Returns:
        Tuple of solutions (x1, x2) or None if no real solutions

    Raises:
        ValueError: If a = 0 (not a quadratic equation)
        TypeError: If coefficients aren't numeric
    """
```

#### Usage Examples:

```python
from quadratic_solver import solve_quadratic_equation

# Example 1: Two real solutions
# Equation: x² - 5x + 6 = 0
result = solve_quadratic_equation(a=1, b=-5, c=6)
if result:
    x1, x2 = result
    print(f"Solutions: x1 = {x1}, x2 = {x2}")  # x1 = 3.0, x2 = 2.0

# Example 2: No real solutions
# Equation: x² + 1 = 0 (complex roots)
result = solve_quadratic_equation(a=1, b=0, c=1)
if result:
    x1, x2 = result
else:
    print("No real solutions")  # Prints this

# Example 3: Error handling
try:
    result = solve_quadratic_equation(a=0, b=5, c=6)  # Invalid!
except ValueError as e:
    print(f"Error: {e}")  # Error: Coefficient 'a' cannot be zero
```

#### Understanding the Discriminant:

The discriminant (Δ) determines the number of real solutions:

```
Δ = b² - 4ac

If Δ > 0: Two different real solutions ✓
If Δ = 0: One real solution (repeated root)
If Δ < 0: No real solutions → returns None
```

#### Complete Example:

```python
# Solve: 2x² + 3x - 2 = 0
result = solve_quadratic_equation(2, 3, -2)
# Δ = 3² - 4(2)(-2) = 9 + 16 = 25
# √Δ = 5
# x1 = (-3 + 5) / 4 = 0.5
# x2 = (-3 - 5) / 4 = -2
# Result: (0.5, -2.0)
```

---

### 4️⃣ **secret_leak.py** - Secure AWS Credential Management

**What it does:** Securely retrieves and manages AWS credentials from environment variables (NOT hardcoded).

**Why it matters:** Demonstrates critical security best practices for handling sensitive authentication data.

#### Key Functions:

```python
def _get_env_variable(name: str) -> str:
    """
    Securely retrieve environment variable.

    Raises:
        ValueError: If variable is missing or empty
    """

def get_aws_credentials() -> dict:
    """
    Retrieve AWS credentials securely from environment.

    Required environment variables:
        AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY
        AWS_DEFAULT_REGION
    """

def connect() -> Optional[bool]:
    """Establish AWS connection with proper error handling."""
```

#### Safe Usage Example:

```python
import os
from secret_leak import get_aws_credentials

# Set environment variables (best practice: use .env file)
os.environ["AWS_ACCESS_KEY_ID"] = "your_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_key"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# Retrieve credentials securely
try:
    creds = get_aws_credentials()
    print(f"Connected to region: {creds['region']}")
    # Use creds safely
except ValueError as e:
    print(f"Configuration error: {e}")
```

#### Security Best Practices:

**✅ DO:**

```python
# Load from environment variables
aws_key = os.getenv("AWS_SECRET_KEY")

# Use .env files with python-dotenv
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("AWS_SECRET_KEY")
```

**❌ DON'T:**

```python
# Never hardcode secrets in source code!
AWS_SECRET_KEY = "AKIA1234567890ABCDEF123"

# Never commit credentials to git!
# Never log sensitive data!
logger.info(f"Key: {aws_secret_key}")
```

#### Error Handling:

```python
try:
    creds = get_aws_credentials()
except ValueError:
    # Handle missing environment variables
    print("Credentials not configured")
```

---

### 5️⃣ **demo.py** - Interactive Demonstration

**What it does:** Interactive demonstration showing all error handling and edge cases in action.

#### Run the Demo:

```bash
python demo.py
```

#### What It Shows:

The demo displays 7 scenarios:

1. **Valid Input** - Works correctly
2. **Original Bug** - [10, 5, 0] - Caught gracefully
3. **Single Zero** - Handled properly
4. **Empty List** - Clear error message
5. **Invalid Type** - String rejected
6. **Negative Numbers** - Works correctly
7. **Boolean Input** - Rejected as invalid

#### Sample Output:

```
======================================================================
FIXED CODE - Handles edge cases gracefully:
======================================================================

1️⃣  Valid input [10, 5, 2]:
   ✅ Success: Average ratio = 26.67

2️⃣  Original bug case [10, 5, 0]:
   ✅ Caught gracefully: Division by zero encountered: cannot divide 100 by 0
```

---

## 🧪 Testing

### Run Unit Tests

```bash
python test_failing_calculator.py
```

### Test Coverage:

- **21 comprehensive unit tests**
- ✅ Happy path scenarios (8 tests) - Normal operation
- ✅ Error handling tests (4 tests) - Edge cases and errors
- ✅ Type validation tests (5 tests) - Type safety
- ✅ Real-world scenarios (3 tests) - Practical usage

### Example Test:

```python
def test_division_by_zero_in_middle():
    """Test that zero in the middle of list is caught.

    This is the exact scenario from the original bug: [10, 5, 0]
    """
    with self.assertRaises(ValueError):
        calculate_average_ratios([10, 5, 0])  # Should raise, not crash
```

### Test Results:

```
Ran 21 tests in 0.008s
OK ✅
```

---

## 📋 Key Concepts Explained

### 1. **Type Hints**

Type annotations clarify what data functions expect and return:

```python
def calculate_average_ratios(numbers: List[float]) -> float:
    # 'numbers' parameter must be a list of floats
    # Function returns a single float value
```

**Benefits:**

- Code is self-documenting
- IDE autocomplete works better
- Catches bugs early
- Makes refactoring safer

### 2. **Error Handling**

Instead of crashing, catch errors and provide helpful context:

```python
if number == 0:
    raise ValueError("Cannot divide 100 by 0")
# Provides context about WHAT is wrong and WHY
```

**vs. unhandled crash:**

```python
ratio = 100 / number  # ❌ Crashes with ZeroDivisionError
```

### 3. **Input Validation**

Check data BEFORE processing:

```python
if not isinstance(number, (int, float)) or isinstance(number, bool):
    raise TypeError("Invalid type: must be int or float")
# Catches invalid data early with clear message
```

### 4. **Secure Logging**

Track application behavior without exposing secrets:

```python
logger.info(f"Processed {len(values)} values")  # Safe ✅

# logger.info(aws_secret_key)  # ❌ NEVER do this!
# logger.info(user_password)   # ❌ NEVER do this!
```

### 5. **Separation of Concerns**

Each function has a single, clear responsibility:

```python
process_values()  # Only computes → Pure function
display_results() # Only prints → Side effect
log_results()     # Only logs → Side effect
```

**Benefits:**

- Easy to test
- Easy to reuse
- Easy to maintain
- Easy to understand

---

## 🚀 Getting Started

### Installation

```bash
# Clone or download the project
cd mcp-student-sandbox

# No external dependencies required!
# Uses only Python standard library
```

### Quick Start

```python
# Example 1: Calculate average ratios
from calculator import calculate_average_ratios
result = calculate_average_ratios([10, 5, 2])
print(f"Result: {result:.2f}")  # 26.67

# Example 2: Process and display values
from spaghetti_logic import process_values, display_results
data = [100, 200, 300]
processed = process_values(data)
display_results(processed)

# Example 3: Solve quadratic equation
from quadratic_solver import solve_quadratic_equation
result = solve_quadratic_equation(1, -5, 6)
if result:
    print(f"Solutions: x1={result[0]}, x2={result[1]}")
```

---

## 💡 Learning Objectives

After studying this project, you'll understand:

- ✅ How to write **clean, readable code** with meaningful names
- ✅ How to handle **errors gracefully** with validation
- ✅ How to write **secure applications** (no hardcoded secrets)
- ✅ How to use **type hints** effectively
- ✅ How to create **comprehensive documentation**
- ✅ How to write **meaningful tests** for edge cases
- ✅ How to **separate concerns** in design
- ✅ How to handle **sensitive data** securely
- ✅ How to implement **secure logging** with rotation

---

## 📚 Additional Documentation

| File                                               | Purpose                                            |
| -------------------------------------------------- | -------------------------------------------------- |
| [SECURITY_AUDIT.md](SECURITY_AUDIT.md)             | Detailed security vulnerability analysis and fixes |
| [SECURITY_FIX_SUMMARY.md](SECURITY_FIX_SUMMARY.md) | Quick reference for security improvements          |
| [ANALYSIS.md](ANALYSIS.md)                         | Root cause analysis of division by zero bug        |
| [SUMMARY.md](SUMMARY.md)                           | Executive summary with deployment checklist        |

---

## 🔄 Evolution of Code Quality

### Example: The Calculator Module

**BEFORE (Vulnerable):**

```python
def average_ratios(numbers):
    total = 0
    for i in range(len(numbers)):
        total += 100 / numbers[i]  # ❌ CRASHES on zero!
    return total / len(numbers)

# Issues:
# - Poor variable names (total, i)
# - No input validation
# - Crashes on division by zero
# - No error message
# - No type hints
# - No documentation
```

**AFTER (Production Quality):**

```python
def calculate_average_ratios(numbers: List[float]) -> float:
    """Calculate average of (100 / number) for each number."""

    if not numbers:
        raise ValueError("Input list cannot be empty")

    ratios = []
    for number in numbers:
        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise TypeError(f"Invalid input type: {type(number)}")
        if number == 0:
            raise ValueError("Cannot divide 100 by 0")

        ratio = 100 / number
        ratios.append(ratio)

    return sum(ratios) / len(ratios)

# Improvements:
# ✅ Clear variable names (numbers, ratios)
# ✅ Comprehensive input validation
# ✅ Zero check before division
# ✅ Descriptive error messages
# ✅ Full type hints
# ✅ Complete docstring
```

---

## ❓ FAQ

**Q: Why do we need type hints?**  
A: They make code self-documenting, enable IDE autocomplete, and help catch bugs early.

**Q: What happens if I divide by zero?**  
A: Instead of crashing, you get a clear `ValueError` message explaining the problem.

**Q: Where are logs stored?**  
A: In the `.logs/` directory with automatic rotation at 5MB to prevent disk bloat.

**Q: Can I hardcode AWS secrets in my code?**  
A: **Never!** Always use environment variables, .env files, or secure credential vaults.

**Q: How many tests should I write?**  
A: Aim for broad coverage: happy paths, edge cases, and error scenarios (as shown with 21 tests).

**Q: What if I need environment-specific configuration?**  
A: Use environment variables (`os.getenv()`) or .env files that are never committed to git.

---

## 🎯 Best Practices Summary

| Practice               | Why It Matters                                  |
| ---------------------- | ----------------------------------------------- |
| Input validation       | Catches bad data early, prevents crashes        |
| Type hints             | Documents code, enables IDE help, catches bugs  |
| Error handling         | Provides context when things go wrong           |
| Separation of concerns | Makes code testable and maintainable            |
| Logging                | Tracks application behavior safely              |
| Unit tests             | Ensures code works as expected in all scenarios |
| Documentation          | Helps others (and future you) understand code   |
| No hardcoded secrets   | Prevents accidental credential exposure         |

---

## 👩‍💻 Author

Developed as part of a Python software engineering learning curriculum focusing on clean code, security, and quality practices.

---

## 📝 License

Educational project - Use freely for learning purposes.

---

**Happy Learning! 🎓**

For questions or improvements, review the supporting documentation files included in this project.
