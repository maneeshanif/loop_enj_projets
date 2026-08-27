#!/usr/bin/env python3
# Buggy code for Project 4 - has a deliberate bug to fix

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    # BUG: Should divide by count, not count + 1
    return total / (count + 1)

def find_max(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def is_even(n):
    """Check if a number is even."""
    # BUG: Should be n % 2 == 0, not n % 2 == 1
    return n % 2 == 1

if __name__ == "__main__":
    # Test the functions
    test_nums = [10, 20, 30, 40, 50]
    print(f"Average: {calculate_average(test_nums)}")  # Should be 30, bug gives 25
    print(f"Max: {find_max(test_nums)}")  # Should be 50
    print(f"Is 4 even? {is_even(4)}")  # Should be True, bug gives False
    print(f"Is 5 even? {is_even(5)}")  # Should be False, bug gives True
