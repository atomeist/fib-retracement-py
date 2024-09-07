def get_fib_retracement(start: float, end: float) -> dict:
    """Calculate Fibonacci retracement levels with 'start' as 0 and 'end' as 1."""
    
    # Fibonacci retracement levels
    levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
    
    # Calculate and format price points based on the retracement levels
    retracements = {}
    for level in levels:
        retracements[level] = round(end + (start - end) * level, 2)
    
    return retracements