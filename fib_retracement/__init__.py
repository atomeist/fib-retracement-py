def get_fib_retracement(start: float, end: float) -> dict:
    """Calculate Fibonacci retracement levels between two points."""
    levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
    retracements = {level: start + (end - start) * level for level in levels}
    return retracements