def put(value, lst):
    for i in range(len(lst)):
        if lst[i] == "":
            lst[i] = value
            return i
    return -1


def remove(value, lst):
    count = 0
    
    for i in range(len(lst)):
        if lst[i] == value:
            lst[i] = ""
            count += 1
    
    return count