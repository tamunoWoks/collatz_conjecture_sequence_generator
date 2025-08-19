# Collatz Conjecture Sequence Generator
A Python program that implements and demonstrates the famous Collatz conjecture (also known as the 3n+1 problem). This mathematical conjecture states that for any positive integer, repeatedly applying a specific set of operations will eventually lead to the number 1.

### The Collatz Conjecture:
The algorithm follows these simple rules:
- If the number is even: divide it by 2 (n // 2).
- If the number is odd: multiply by 3 and add 1 (3n + 1).
- Repeat until the sequence reaches 1.

### Features:
- **Interactive Input:** Users can input any positive integer.
- **Error Handling:** Comprehensive input validation with user-friendly error messages.
- **Clean Output:** Sequences displayed in a readable, space-separated format.
- **Robust Implementation:** Handles various edge cases and unexpected inputs.
- **Well-Documented:** Clear comments and docstrings throughout the code.

### Error Handling:
The program handles various error scenarios:
1. Non-integer input.
2. Non-positive integers.
3. Keyboard interrupts.
