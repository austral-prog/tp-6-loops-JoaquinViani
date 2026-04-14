# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    
    if n <= 0:
        return 0

    return n * (n + 1) // 2 

def sum_evens(n):

    if n <= 0:
        return 0
    return sum(i for i in range(2, n + 1, 2))


def factorial(n):
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
