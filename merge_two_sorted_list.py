def merge_list(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    
    result = []
    if len(lst1) < len(lst2):
        lst1, lst2 = lst2, lst1
    indexI, indexJ = 0, 0
    while True:
        if indexI == len(lst1) or indexJ == len(lst2):
            break
        if (lst1[indexI] < lst2[indexJ]):
            result.append(lst1[indexI])
            indexI+=1
            continue
        else:
            result.append(lst2[indexJ])
            indexJ+=1
            continue

    for i in range(indexI, len(lst1)):
        result.append(lst1[i]) 
    for i in range(indexJ, len(lst2)):
        result.append(lst2[i]) 

    return result