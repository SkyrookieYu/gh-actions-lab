"""Simple calculator module."""


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two numbers."""
    return a - b


def divide(a: int, b: int) -> float:
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
