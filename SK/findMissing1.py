def findMissing(arr):
    sum = 0
    for x in arr:
        sum += x
    return (((len(arr) +1) * len(arr)) / 2) - sum
    raise ValueError(msg= "No missing element")

