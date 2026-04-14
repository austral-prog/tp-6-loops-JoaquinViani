def enumerate_list(lst):
    result = []
    index = 0
    
    for item in lst:
        if item != "":
            result.append(f"{index}. {item}")
            index += 1
    
    return result


def enumerate_backwards(lst):
    result = []
    index = 0
    
    for item in lst:
        if item != "":
            reversed_item = item[::-1]
            result.append(f"{index}. {reversed_item}")
            index += 1
    
    return result
