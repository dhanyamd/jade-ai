"""Calculator module supporting basic arithmetic operations."""


def calculator(a: float, operation: str, b: float) -> float:
    """Perform a basic arithmetic operation on two numbers.

    Args:
        a: First operand.
        operation: One of '+', '-', '*', '/'.
        b: Second operand.

    Returns:
        Result of the operation.

    Raises:
        ValueError: If the operation is unsupported or division by zero occurs.
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")
