def stray(arr):

    return int(''.join([str(x) for x in arr if arr.count(x) == 1 ]))
stray([1, 1, 1, 1, 1, 1, 2])