def countdown(n):

    if n < 0:
        return []
    
    result = []
    for i in range(n, -1, -1):
        result.append(i)
    
    return result


def double_until(limit):

    if limit < 1:
        return []
    
    result = []
    value = 1
    
    while value <= limit:
        result.append(value)
        value *= 2
    
    return result