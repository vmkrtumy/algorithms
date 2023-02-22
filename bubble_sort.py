def is_sorted(sort):
    i = 0
    l = len(sort)
    while i < l - 1:
        if sort[i] > sort[i+1]:
            return 0
        i+=1
    return 1

def bubble_sort(sort):
    temp = 0
    i = 0
    len1 = len(sort)
    if is_sorted(sort):
        return 1
    while i < len1 - 1:
        if sort[i] > sort[i+1]:
            temp = sort[i]
            sort[i] = sort[i+1]
            sort[i+1] = temp
        if is_sorted(sort):
            return 1
        i+=1
    if bubble_sort(sort):
        return 1
