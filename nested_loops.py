def flatten(matrix):

    result = []
    
    for row in matrix:
        for value in row:
            result.append(value)
    
    return result


def row_sums(matrix):

    result = []
    
    for row in matrix:
        total = 0
        for value in row:
            total += value
        result.append(total)
    
    return result


def col_sums(matrix):

    if not matrix:
        return []
    
    num_cols = len(matrix[0])
    result = [0] * num_cols
    
    for row in matrix:
        for i in range(num_cols):
            result[i] += row[i]
    
    return result