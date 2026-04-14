# Replace the "ANSWER HERE" for your answer

def power(base, exp):

    result = 1
    for _ in range(exp):
        result *= base
    return result


def sum_of_powers(base, max_exp):

    total = 0
    for exp in range(max_exp + 1):
        total += power(base, exp)
    return total
