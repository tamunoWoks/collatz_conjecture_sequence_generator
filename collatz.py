def collatz(number):
    """
    Applies the Collatz conjecture formula to a given number.
    
    Args:
        number (int): The input number to process
        
    Returns:
        int: The result of the Collatz operation
    """
    # Check if the number is even
    if number % 2 == 0:
        result = number // 2  # Integer division by 2 for even numbers
    else:
        result = 3 * number + 1  # 3n+1 formula for odd numbers
