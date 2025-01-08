def divide(a: int, b: int) -> float:
    """
    Returns the result of a division operation between two numbers

    Args: 
     a(int) : numerator
     b(int) : denominator

    Returns:
     float : the result of the division operation

    Raises:
     ZeroDivisionError : If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("You cant divide by zero!")
    return a / b