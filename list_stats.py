# ---- Funciones provistas (NO modificar) ----

def find_min(numbers):
    """Dada una lista de numeros, retorna el menor valor."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    """Dada una lista de numeros, retorna el mayor valor."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# ---- Funciones a implementar ----

def range_of(numbers):
    return find_max(numbers) - find_min(numbers)


def average(numbers):
    if not numbers:
        return 0.0
    
    total = 0
    for num in numbers:
        total += num
    
    avg = total / len(numbers)
    return round(avg, 1)


def describe(numbers):
    if not numbers:
        return "Empty list"
    
    minimum = find_min(numbers)
    maximum = find_max(numbers)
    rng = range_of(numbers)
    avg = average(numbers)
    
    return f"Min:{minimum} Max:{maximum} Range:{rng} Avg:{avg}"