def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly n 'H' characters
    in the file using only Copy All and Paste operations.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if n cannot be achieved.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
