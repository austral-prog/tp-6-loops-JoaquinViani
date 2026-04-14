def find_min(numbers):

    minimum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
    
    return minimum


def find_max(numbers):

    maximum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
    
    return maximum


def count_negatives(numbers):

    count = 0
    
    for num in numbers:
        if num < 0:
            count += 1
    
    return count