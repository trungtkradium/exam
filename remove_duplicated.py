def remove_duplicates(lst):
    map = {}
    result = []
    for val in lst:
        if str(val) in map:
            if map[str(val)] == 1:
                result.append(val)
            map[str(val)] = map[str(val)] + 1
        else:
            map[str(val)] = 1
    return result
