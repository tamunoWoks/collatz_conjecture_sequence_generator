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

    # Print the result with space separator and return it
    print(result, end=' ')
    return result

def main():
    """
    Main program that runs the Collatz sequence until it reaches 1.
    Handles user input and error checking.
    """

    try:
        # Get user input and convert to integer
        user_input = input("Enter a positive integer: ")
        number = int(user_input)

        # Validate that the number is positive
        if number <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return   

        print(f"Collatz sequence for {number}:", end=' ')
        print(number, end=' ')  # Print the starting number

        # Continue applying Collatz function until we reach 1
        while number != 1:
            number = collatz(number)

        print()  # Add a newline at the end for clean output
