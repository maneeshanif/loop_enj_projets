def sum_first_n(n):
    total = 0
    for i in range(n + 1):  # Bug: off-by-one error
        total += i
    return total

def get_length(items):
    return len(items)

def safe_divide(a, b):
    return a / b  # Bug: division by zero risk