def equalizeArray(arr):
    ary = []
    array = list(dict.fromkeys(arr))
    for i in array:
        ary.append(arr.count(i))
    return len(arr) - max(ary) 
