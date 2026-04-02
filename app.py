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


def multiply(a, b):
    # 故意寫得有問題：沒有 type hints、沒有 docstring、
    # 而且 edge case 沒處理（例如超大數字溢位）
    result = 0
    for i in range(b):
        result += a
    return result


def power(base, exp):
    # 故意用遞迴但沒有終止條件的邊界檢查
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
    # 問題：負數指數會無限遞迴
